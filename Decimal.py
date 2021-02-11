def bin_to_dec(Binary):
    i = 0
    sum = 0

    while Binary != 0:
        rem = Binary % 10
        sum = sum + (pow(2, i)*rem)
        Binary = Binary // 10
        i += 1

    return sum
