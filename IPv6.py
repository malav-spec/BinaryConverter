import Hexadecmial as hex


def format_list(elements):
    i = 1
    ip = ""
    ip = ip + elements[0]
    while i <= len(elements) - 1:
        ip = ip + ":" + elements[i]
        i += 1
    return ip


def bin_to_ipv6(in_binary):
    in_binary = str(in_binary)
    bin_list = in_binary.split(' ')
    i = 0
    final_ip = []

    while i <= len(bin_list) - 1:
        convert = hex.bin_to_hex(int(bin_list[i]))
        convert = str(convert)
        final_ip.append(convert)
        i += 1

    ip = format_list(final_ip)
    return ip
