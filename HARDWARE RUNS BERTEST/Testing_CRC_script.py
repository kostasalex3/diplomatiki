import subprocess
import re
import shutil
import time

def log_results(filename, test_name, crc_error_line, crc_format_error_line, duration):
    with open(filename, "a") as f:
        f.write(f"\n=== Results for {test_name} ===\n")
        f.write(f"Duration: {duration:.2f} seconds\n")
        f.write(f"{crc_error_line}\n")
        f.write(f"{crc_format_error_line}\n")
        f.write("="*40 + "\n")

def strip_ansi_escape_codes(text):
    ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    output = output.decode("utf-8")
    output = strip_ansi_escape_codes(output)
    if error:
        print("Error:", error.decode("utf-8"))
    return output

def main():
    log_file = "CRC_RUN_RESULTS.txt"
    start_bias = 1000
    end_bias = 80

    template_xml = "CMSIT_RD53Bv2_template.xml"
    target_xml = "CMSIT_RD53Bv2.xml"
    shutil.copy(template_xml, target_xml)
    
    total_start_time = time.time()

    dac_cml_bias = start_bias
    
    while dac_cml_bias >= end_bias:
        print(f"\nRunning with DAC_CML_BIAS_0 = {dac_cml_bias}")
        
        print("Resetting DAQ with cmsittxt.sh...")
        run_command("./cmsittxt.sh")

        print("Running reset command...")
        run_command("CMSITminiDAQ -f CMSIT_RD53Bv2.xml -r")

        # pixelalive scan and capture output
        print("Running pixelalive scan...")
        start_time = time.time()  # Start timer for pixelalive
        pixelalive_output = run_command("CMSITminiDAQ -f CMSIT_RD53Bv2.xml -c pixelalive")
        duration_pixelalive = time.time() - start_time  # Duration for pixelalive

        crc_error_line = ""
        crc_format_error_line = ""
        for line in pixelalive_output.splitlines():
            if "CRC ERROR FOR" in line:
                crc_error_line = line.strip()
            if "CRC FORMAT ERRORS ARE" in line:
                crc_format_error_line = line.strip()
        
        log_results(log_file, f"PixelAlive Test at DAC_CML_BIAS_0 = {dac_cml_bias}", crc_error_line, crc_format_error_line, duration_pixelalive)
        print(f"PixelAlive Test CRC Errors: {crc_error_line}")
        print(f"PixelAlive Test CRC Format Errors: {crc_format_error_line}")
        print(f"PixelAlive Test Duration: {duration_pixelalive:.2f} seconds")

        print("Running reset command before bertest...")
        run_command("CMSITminiDAQ -f CMSIT_RD53Bv2.xml -r")

        print("Running bertest scan...")
        start_time = time.time()
        bertest_output = run_command("CMSITminiDAQ -f CMSIT_RD53Bv2.xml -c bertest")
        duration_bertest = time.time() - start_time  # Duration for bertest

        crc_error_line = ""
        crc_format_error_line = ""
        for line in bertest_output.splitlines():
            if "CRC ERROR FOR" in line:
                crc_error_line = line.strip()
            if "CRC FORMAT ERRORS ARE" in line:
                crc_format_error_line = line.strip()
        
        log_results(log_file, f"BERTest at DAC_CML_BIAS_0 = {dac_cml_bias}", crc_error_line, crc_format_error_line, duration_bertest)
        print(f"BERTest CRC Errors: {crc_error_line}")
        print(f"BERTest CRC Format Errors: {crc_format_error_line}")
        print(f"BERTest Duration: {duration_bertest:.2f} seconds")

        with open(target_xml, "r") as file:
            xml_data = file.read()
        xml_data = re.sub(r"(DAC_CML_BIAS_0\s*=\s*\")(\d+)", lambda m: f'{m.group(1)}{int(m.group(2)) - 100}', xml_data)
        with open(target_xml, "w") as file:
            file.write(xml_data)

        dac_cml_bias -= 50

    total_duration = time.time() - total_start_time
    print(f"\nTotal Elapsed Time: {total_duration:.2f} seconds")
    with open(log_file, "a") as f:
        f.write(f"\nTotal Elapsed Time: {total_duration:.2f} seconds\n")

if __name__ == "__main__":
    main()

