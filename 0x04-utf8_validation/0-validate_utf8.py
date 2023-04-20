#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Determine if a given data set represents a valid
    UTF-8 encoding.
    """
    no_of_bytes = 0

    mk1 = 1 << 7
    mk2 = 1 << 6

    for i in data:

        mk_and_byte = 1 << 7

        if no_of_bytes == 0:
            while mk_and_byte & i:
                no_of_bytes += 1
                mk_and_byte = mk_and_byte >> 1

            if no_of_bytes == 0:
                continue

            if no_of_bytes == 1 or no_of_bytes > 4:
                return False

        else:
            if not (i & mk1 and not (i & mk2)):
                    return False

        no_of_bytes -= 1

    if no_of_bytes == 0:
        return True

    return False
