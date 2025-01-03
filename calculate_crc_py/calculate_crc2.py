def crc32_mpeg2(data: bytes) -> int:
    """
    Calculate the CRC32 MPEG-2 checksum of the given data.
    The polynomial used is 0x04C11DB7 and the initial value is 0xFFFFFFFF.
    
    :param data: Input data as bytes
    :return: The CRC32 checksum as an integer
    """
   
    polynomial = 0x04C11DB7
    crc = 0xFFFFFFFF

    print(f"Initial CRC value: {crc:08X}")

   
    for byte_index, byte in enumerate(data):
        print(f"\nProcessing byte {byte_index+1}: {byte:02X} ({byte})")

       
        before_xor = crc
        crc ^= (byte << 24)
        print(f"  XOR {before_xor:08X} with {byte << 24:08X} (byte << 24): {crc:08X}")

        
        for bit in range(8):
            before_shift = crc
            msb_bit = (crc & 0x80000000) >> 31

            
            print(f"    Bit {bit+1}: Concatenating {'1' if msb_bit else '0'}")

            if msb_bit:
                crc = (crc << 1) ^ polynomial
                print(f"    MSB is set, shift left and XOR with polynomial:")
                print(f"    {before_shift:08X} << 1 = {(before_shift << 1) & 0xFFFFFFFF:08X}")
                print(f"    XOR with {polynomial:08X}: {crc:08X}")
            else:
                crc <<= 1
                print(f"    MSB is not set, just shift left:")
                print(f"    {before_shift:08X} << 1 = {crc:08X}")

            crc &= 0xFFFFFFFF
            print(f"    After bit {bit+1}: {crc:08X}")

    return crc


data_hex = "4f3b1a9d5c6e7f8a"
data_bytes = bytes.fromhex(data_hex)

crc_result = crc32_mpeg2(data_bytes)
print(f"\nFinal CRC32 (MPEG-2) for {data_hex}: {crc_result:08X}")

