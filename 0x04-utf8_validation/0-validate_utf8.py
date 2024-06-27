#!/usr/bin/python3
"""0-validate_utf8 module"""


def validUTF8(data):
    """Determine if a given data set represents a valid UTF-8 encoding"""
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Masks to check the most significant bit(s)
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        # Mask to check the most significant byte(s) in `num`
        mask = 1 << 7

        if n_bytes == 0:
            # Count the number of leading 1s in the byte
            while mask & num:
                n_bytes += 1
                mask >>= 1

            # 1 byte character (ASCII), continue
            if n_bytes == 0:
                continue

            # If more than 4 bytes or less than 2 bytes, return False
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check if the byte starts with '10'
            if not (num & mask1 and not (num & mask2)):
                return False

        n_bytes -= 1

    return n_bytes == 0
