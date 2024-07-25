#!/usr/bin/python3
""" UTF-8 Validation
"""


def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the leading bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Get the 8 least significant bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the current character
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            # 1-byte character
            if num_bytes == 0:
                continue

            # Invalid scenarios
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # The byte must be of the form 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the number of bytes
        num_bytes -= 1

    # If num_bytes is not zero, it means we have incomplete characters
    return num_bytes == 0
