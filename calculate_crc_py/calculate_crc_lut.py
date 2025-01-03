#!/usr/bin/env python
# CRC-32 MPEG-2 implementation using custom polynomial (0x04C11DB7)

import sys

POLYNOMIAL = 0x04C11DB7


table = []


def init_crc32_mpeg2_table():
  
    global table
    table = []
    print(f"Generating CRC-32 MPEG-2 LUT with polynomial: 0x{POLYNOMIAL:08X}")
    
    # Generate CRC32 lookup table
    for i in range(256):
        crc = i << 24
        for bit in range(8):
            if crc & 0x80000000:
                crc = (crc << 1) ^ POLYNOMIAL
            else:
                crc <<= 1
            crc &= 0xFFFFFFFF  # Keep CRC as 32-bit
        table.append(crc)
        print(f"Table[{i:02X}] = 0x{crc:08X}")  # Print each LUT entry


def calc_crc32_mpeg2(data):
 
    crc = 0xFFFFFFFF  # Initial value for CRC
    print("\nStarting CRC-32 calculation...")
    print(f"Initial CRC value: 0x{crc:08X}")
    
    for index, byte in enumerate(data):
        table_idx = (crc >> 24) ^ byte
        print(f"\nProcessing byte {index + 1}: 0x{byte:02X}")
        print(f"Table index: {table_idx:02X}")
        crc = ((crc << 8) & 0xFFFFFFFF) ^ table[table_idx]
        print(f"Updated CRC: 0x{crc:08X}")
    
    print(f"\nFinal CRC value (before any XOR): 0x{crc:08X}")
    return crc


def main(input_data):
    
    init_crc32_mpeg2_table()

  
    print("\nInput data:")
    print(" ".join([f"0x{byte:02X}" for byte in input_data]))

   
    crc_result = calc_crc32_mpeg2(input_data)
    print(f"\nCRC-32 MPEG-2 Result: 0x{crc_result:08X}")


if __name__ == '__main__':
    if len(sys.argv) > 1:
       
        input_data = bytearray.fromhex(sys.argv[1])
    else:
       
        input_data = bytearray([0x4f, 0x3b, 0x1a, 0x9d, 0x5c, 0x6e, 0x7f, 0x8a])

    main(input_data)

