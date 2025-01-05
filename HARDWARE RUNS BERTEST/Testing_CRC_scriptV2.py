import re
import subprocess
import shutil
import time

class Colors:
    RESET = "\033[0m"
    BOLD_GREEN = "\033[1;32m"
    CYAN = "\033[1;36m"
    YELLOW = "\033[1;33m"
    MAGENTA = "\033[1;35m"

def log_results(filename, test_name, crc_error_line, crc_format_error_line, duration):
    with open(filename, "a") as f:
        f.write(f"\n=== Results for {test_name} ===\n")
        f.write(f"Duration: {duration:.2f} seconds\n")
        if crc_error_line:
            f.write(f"{crc_error_line}\n")
        if crc_format_error_line:
            f.write(f"{crc_format_error_line}\n")
        f.write("=" * 40 + "\n")

def strip_ansi_escape_codes(text):
    ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)

def clean_crc_line(line):
    line = re.sub(r'\|.*?\|[A-Z]\|', '', line).strip()
    return line

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    output = output.decode("utf-8")
    output = strip_ansi_escape_codes(output)
    if error:
        print("Error:", error.decode("utf-8"))
    return output

def run_pixelalive_for_one_hour(target_xml, log_file, dac_cml_bias):
    total_pixelalive_duration = 0
    pixelalive_test_count = 0

    while total_pixelalive_duration < 3600:  # 1 hour
        print(f"{Colors.CYAN}Running pixelalive scan #{pixelalive_test_count + 1}...{Colors.RESET}")
        start_time = time.time()
        pixelalive_output = run_command(f"CMSITminiDAQ -f {target_xml} -c pixelalive")
        duration_pixelalive = time.time() - start_time

        crc_error_line = ""
        crc_format_error_line = ""
        for line in pixelalive_output.splitlines():
            if "CRC ERROR FOR" in line:
                crc_error_line = clean_crc_line(line)
            if "CRC FORMAT ERRORS ARE" in line:
                crc_format_error_line = clean_crc_line(line)

        log_results(
            log_file,
            f"PixelAlive Test at DAC_CML_BIAS_0 = {dac_cml_bias} (Run #{pixelalive_test_count + 1})",
            crc_error_line,
            crc_format_error_line,
            duration_pixelalive
        )

        print(f"{Colors.YELLOW}PixelAlive Test #{pixelalive_test_count + 1} Duration: {duration_pixelalive:.2f} seconds{Colors.RESET}")
        print(f"{Colors.MAGENTA}CRC Errors: {crc_error_line}{Colors.RESET}")
        print(f"{Colors.MAGENTA}CRC Format Errors: {crc_format_error_line}{Colors.RESET}")

        total_pixelalive_duration += duration_pixelalive
        pixelalive_test_count += 1

        # avoid overshooting 1 hour
        if total_pixelalive_duration + 16.10 > 3600:
            break

def main():
    log_file = "CRC_RUN_RESULTS.txt"
    start_bias = 1000
    high_step = 100
    low_step = 5
    end_bias = 80

    template_xml = "CMSIT_RD53Bv2_template.xml"
    target_xml = "CMSIT_RD53Bv2.xml"
    shutil.copy(template_xml, target_xml)
    
    total_start_time = time.time()
    dac_cml_bias = start_bias

    print(f"{Colors.CYAN}Resetting DAQ with cmsittxt.sh...{Colors.RESET}")
    run_command("./cmsittxt.sh")
    print(f"{Colors.CYAN}Running reset command...{Colors.RESET}")
    run_command("CMSITminiDAQ -f CMSIT_RD53Bv2.xml -r")

    while dac_cml_bias >= end_bias:
        print(f"{Colors.BOLD_GREEN}\nRunning with DAC_CML_BIAS_0 = {dac_cml_bias}{Colors.RESET}")

        print(f"{Colors.CYAN}Running pixelalive scans for 1 hour...{Colors.RESET}")
        run_pixelalive_for_one_hour(target_xml, log_file, dac_cml_bias)

        print(f"{Colors.CYAN}Running bertest scan...{Colors.RESET}")
        start_time = time.time()
        bertest_output = run_command("CMSITminiDAQ -f CMSIT_RD53Bv2.xml -c bertest")
        duration_bertest = time.time() - start_time

        crc_error_line = ""
        crc_format_error_line = ""
        for line in bertest_output.splitlines():
            if "CRC ERROR FOR" in line:
                crc_error_line = clean_crc_line(line)
            if "CRC FORMAT ERRORS ARE" in line:
                crc_format_error_line = clean_crc_line(line)

      
        log_results(
            log_file,
            f"BERTest at DAC_CML_BIAS_0 = {dac_cml_bias}",
            crc_error_line,
            crc_format_error_line,
            duration_bertest
        )

        print(f"{Colors.YELLOW}BERTest Duration: {duration_bertest:.2f} seconds{Colors.RESET}")
        print(f"{Colors.MAGENTA}CRC Errors: {crc_error_line}{Colors.RESET}")
        print(f"{Colors.MAGENTA}CRC Format Errors: {crc_format_error_line}{Colors.RESET}")

       
        decrement = low_step if dac_cml_bias <= 100 else high_step
        new_bias_value = dac_cml_bias - decrement
        with open(target_xml, "r") as file:
            xml_data = file.read()
        xml_data = re.sub(r"(DAC_CML_BIAS_0\s*=\s*\")(\d+)", lambda m: f'{m.group(1)}{new_bias_value}', xml_data)
        with open(target_xml, "w") as file:
            file.write(xml_data)

        dac_cml_bias -= decrement

    total_duration = time.time() - total_start_time
    with open(log_file, "a") as f:
        f.write(f"\nTotal Elapsed Time: {total_duration:.2f} seconds\n")

if __name__ == "__main__":
    main()

