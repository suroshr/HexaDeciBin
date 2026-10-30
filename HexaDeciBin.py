def deci_to_bin(x):
    return format(x, 'b')

def deci_to_hex(x):
    return format(x, 'X')

def bin_to_deci(x):
    return int(x, 2)

def hex_to_deci(x):
    return int(x, 16)


# Two's Complement Functions
def deci_to_twos(x, bits):
    if bits < 2:
        raise ValueError
    if x < -(2 ** (bits - 1)) or x > (2 ** (bits - 1)) - 1:
        raise ValueError
    return format(x & (2 ** bits - 1), f'0{bits}b')

def twos_to_deci(x, bits):
    if bits < 2:
        raise ValueError
    if len(x) != bits or any(d not in "01" for d in x):
        raise ValueError
    value = int(x, 2)
    if value >= 2 ** (bits - 1):
        value -= 2 ** bits
    return value


print("Welcome to HexaDeciBin!")
print("Decimal, Binary, Hexadecimal or Two's Complement")

while True:

    start = input("\nEnter the starting base (dec/bin/hex/twos): ").strip().lower()

    if start not in ["dec", "bin", "hex", "twos"]:
        print("Invalid starting base.")
        continue

    final = input("Enter the final base (dec/bin/hex/twos): ").strip().lower()

    if final not in ["dec", "bin", "hex", "twos"]:
        print("Invalid final base.")

    else:
        try:
            # Convert input to decimal
            if start == "twos":
                bits = int(input("Enter the bit width: "))
                number = input("Enter the two's complement number: ").strip()
                value = twos_to_deci(number, bits)

            elif start == "dec":
                number = input("Enter the decimal number: ").strip()
                value = int(number)

            elif start == "bin":
                number = input("Enter the binary number: ").strip()
                value = bin_to_deci(number)

            elif start == "hex":
                number = input("Enter the hexadecimal number: ").strip()
                value = hex_to_deci(number)

            # Convert decimal to final base
            if final == "dec":
                result = str(value)

            elif final == "bin":
                result = deci_to_bin(value)

            elif final == "hex":
                result = deci_to_hex(value)

            else:
                bits = int(input("Enter the bit width: "))
                result = deci_to_twos(value, bits)

            print(f"Result ({final}):", result)

        except ValueError:
            print("Invalid number, bit width or value outside the allowed range.")

    another = input("\nWould you like to convert another number? (y/n): ").strip().lower()

    if another != "y":
        print("Goodbye!")
        break