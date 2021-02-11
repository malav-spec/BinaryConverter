import Decimal as dec


def get_four(number):
    count = 0
    i = 0
    sum = 0

    while count != 4:
        rem = number % 10
        sum = sum + pow(10, i) * (rem)
        i += 1
        number = number // 10
        count += 1

    return sum, number


def bin_to_char(number):
    conv = {1010: "A", 1011: "B", 1100: "C", 1101: "D", 1110: "E", 1111: "F"}
    return conv[number]


def bin_to_hex(binary):
    i = 0
    sum = 0
    hex_num = ""

    while binary != 0:
        sum, binary = get_four(binary)
        convert = dec.bin_to_dec(sum)

        if convert > 9:
            convert = bin_to_char(sum)
        else:
            convert = str(convert)

        hex_num = convert + hex_num


    return hex_num
