# Python Script to Generate CRC32 LUT Values
import zlib

def generate_crc32_table(polynomial=0x04C11DB7):
    crc32_table = []
    for byte in range(256):
        crc = byte << 24
        for _ in range(8):
            if crc & 0x80000000:
                crc = (crc << 1) ^ polynomial
            else:
                crc <<= 1
        crc32_table.append(crc & 0xFFFFFFFF)
    return crc32_table

def format_crc32_table_for_vhdl(crc32_table):
    vhdl_lut = "signal crc_lut : lut_array := (\n"
    for i, crc in enumerate(crc32_table):
        vhdl_lut += f'    x"{crc:08X}"'
        if i < len(crc32_table) - 1:
            vhdl_lut += ","
        vhdl_lut += "\n"
    vhdl_lut += ");\n"
    return vhdl_lut

# Generate CRC32 LUT
crc32_table = generate_crc32_table()

# Format LUT for VHDL
vhdl_lut = format_crc32_table_for_vhdl(crc32_table)

# Output to a file or print to console
with open("crc32_lut_vhdl.txt", "w") as f:
    f.write(vhdl_lut)

print(vhdl_lut)  # To display the output as well

