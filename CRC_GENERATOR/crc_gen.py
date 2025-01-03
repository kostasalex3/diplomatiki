import subprocess
import os

def generate_crc_vhdl(output_file, polynomial="0x04C11DB7", bus_width=256):

    poly_expanded = (
        "x^32 + x^26 + x^23 + x^22 + x^16 + x^12 + x^11 + "
        "x^10 + x^8 + x^7 + x^5 + x^4 + x^2 + x + 1"
    )
    
    cmd = ["./crcgen_run","-P", poly_expanded,"-B", str(bus_width),"-V"]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        with open(output_file, "w") as vhdl_file:
            vhdl_file.write(result.stdout)
        print(f"VHDL code generated successfully and saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error generating VHDL code: {e.stderr}")

if __name__ == "__main__":
    output_vhdl_file = "crc256_generated.vhd"
    generate_crc_vhdl(output_vhdl_file)

