def crc32_shift_24_bit(data: bytes) -> int:
    """
    Calculate the CRC32 using the logic of shifting by 24 bits for each byte of input data.
    
    :param data: Input data as bytes
    :return: The CRC32 checksum as an integer
    """
    
    polynomial = 0x04C11DB7
    crc = 0xFFFFFFFF

    print(f"Initial CRC value: {crc:08X}")

    for byte_index, byte in enumerate(data):
        crc ^= (byte << 24)  # Shift the byte left by 24 bits into the MSB
        print(f"\nProcessing byte {byte_index + 1}: {byte:02X}")
        print(f"  After XOR with MSB: {crc:08X}")

        for bit in range(8):
            if (crc & 0x80000000) != 0:
                crc = (crc << 1) ^ polynomial
                print(f"    MSB is set, shift left and XOR with polynomial: {crc:08X}")
            else:
                crc <<= 1
                print(f"    MSB is not set, shift left: {crc:08X}")
            
            crc &= 0xFFFFFFFF

   
    return crc

input_hex = "a7c3e9f1d4b5a6c29f678073"
input_bytes = bytes.fromhex(input_hex)

crc_result = crc32_shift_24_bit(input_bytes)
print(f"\nFinal CRC32 (using 24-bit shifts) for {input_hex}: {crc_result:08X}")

