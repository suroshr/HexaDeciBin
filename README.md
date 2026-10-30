# HexaDeciBin

A simple program that converts numbers between **decimal**, **binary**, **hexadecimal** and **two's complement**.

This is my first Python project. I made it to practice for my digital logic classes in electrical engineering, where we change numbers from one base to another a lot.

## What it can do

- Convert a number from any of these bases to any other: decimal, binary, hex, two's complement
- Two's complement works with any number of bits (8, 16, 32, etc.)
- Tells you if a number is too big or too small for the number of bits you picked
- Doesn't crash if you type something wrong. It just shows an error and lets you try again.

## How to run it

You need Python 3 installed.

```bash
python HexaDeciBin.py
```

Then answer the questions on the screen. For the bases, type `dec`, `bin`, `hex` or `twos`.

## Example

```
Welcome to HexaDeciBin!
Decimal, Binary, Hexadecimal or Two's Complement

Enter the starting base (dec/bin/hex/twos): dec
Enter the final base (dec/bin/hex/twos): bin
Enter the decimal number: 42
Result (bin): 101010

Would you like to convert another number? (y/n): y

Enter the starting base (dec/bin/hex/twos): dec
Enter the final base (dec/bin/hex/twos): twos
Enter the decimal number: -5
Enter the bit width: 8
Result (twos): 11111011

Would you like to convert another number? (y/n): n
Goodbye!
```

## How it works

The program always changes the number to decimal first, then to the base you want.

```
your number  ->  decimal  ->  result
```

This keeps the code short. Each base only needs two functions: one to go to decimal, and one to come back from decimal.

| Base | To decimal | From decimal |
|---|---|---|
| Binary | `bin_to_deci` | `deci_to_bin` |
| Hexadecimal | `hex_to_deci` | `deci_to_hex` |
| Two's complement | `twos_to_deci` | `deci_to_twos` |

**Two's complement, in short:**
- If the first bit is `1`, the number is negative.
- Example with 8 bits: `11111011` is 251 as a normal number. Since the first bit is 1, you subtract 256. So 251 - 256 = **-5**.

## Flowchart

![Flowchart](HexaDeciBin_FlowChart.png)

There's also a PDF version: [`HexaDeciBin_FlowChart.pdf`](HexaDeciBin_FlowChart.pdf)

## Good to know

- With 8 bits, two's complement only goes from -128 to 127. So `FF` (255) won't fit in 8 bits. Use 16 bits instead.
- Negative numbers in normal binary or hex just get a minus sign (like `-101`). If you want the real bits, use two's complement.

## What I learned

- How to use `try/except` so the program doesn't crash on bad input
- Going through decimal first makes the code shorter and easier to add to
- How two's complement works with real bits

## Ideas for later

- Add octal (base 8)
- Show the steps of the conversion, like we do by hand in class
- Give a different error message for each kind of mistake
