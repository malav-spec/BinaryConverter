import Decimal as dec


def get_three(number):
    count = 0
    i = 0
    sum = 0

    while count != 3:
        rem = number % 10
        sum = sum + pow(10, i) * (rem)
        i += 1
        number = number // 10
        count += 1

    return sum, number


def bin_to_oct(binary):
    i = 0
    sum = 0
    oct_num = ""

    while binary != 0:
        sum, binary = get_three(binary)

        convert = dec.bin_to_dec(sum)
        convert = str(convert)

        oct_num = convert + oct_num
        
    return oct_num
