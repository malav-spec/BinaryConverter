import Decimal as dec
import Hexadecmial as hex
import Octal as oct
import IPv4 as ip4
import IPv6 as ip6

if __name__ == '__main__':

    print("Session start.")
    print("0. Exit session")
    print("1. Binary -> Decimal")
    print("2. Binary -> Hexadecimal")
    print("3. Binary -> Octal")
    print("4. Binary -> IPv4")
    print("5. Binary -> IPv6")
    print("\n")

    while True:
        option = input("Select the conversion you want: ")

        option = int(option)

        if option == 1:

            bin = input("Enter the binary: ")
            bin = int(bin)
            x = dec.bin_to_dec(bin)
            print("Decimal: ", x)
            print("\n")

        elif option == 2:
            bin = input("Enter the binary: ")
            bin = int(bin)
            print("Hexadecimal: " + "0x" + hex.bin_to_hex(bin))
            print("\n")

        elif option == 3:
            bin = input("Enter the binary: ")
            bin = int(bin)
            print("Octal: " + oct.bin_to_oct(bin))
            print("\n")

        elif option == 4:
            bin = input("Enter the binary: ")
            print("IPv4 address: " + ip4.bin_to_ipv4(bin))

        elif option == 5:
            bin = input("Enter the binary: ")
            print("IPv6 address: " + ip6.bin_to_ipv6(bin))

        elif option == 0:
            print("Session end.")
            exit()