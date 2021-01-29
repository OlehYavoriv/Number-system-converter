import math
print("Enter from which number system we convert:")
system_first = int(input())
print("Input number:")
number = int(input())
print("Enter in which number system we convert:")
system_second = int(input())

if system_first == 2 and system_second == 10:
    def bin_dec(number):
        dec_num = 0
        power = 0
        while number > 0:
            dec_num += 2 ** power * (number % 10)
            number //= 10
            power += 1
        print("Result:", dec_num)
    bin_dec(number)


if system_first == 2 and system_second == 8:
    def bin_oct(number):
        octal = 0
        decimal = 0
        i = 0
        while number != 0:
            decimal += int((number % 10) * math.pow(2, i))
            i = i + 1
            number = int(number / 10)
        i = 1
        while decimal != 0:
            octal += (decimal % 8) * i
            decimal = int(decimal / 8)
            i *= 10
        print("Result:", octal, end='')
        return decimal
    bin_oct(number)


def str_from_end(string, size):
    result = []
    i = len(string)
    while i > 0:
        if i - size > 0:
            result.append(string[i - size:i])
        else:
            result.append(string[0:i])
        i -= size
    return result


table = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6',
              '0111': '7', '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D',
              '1110': 'E', '1111': 'F'}


if system_first == 2 and system_second == 16:
    def bin_hex(number):
        binary = (str(number))
        result = str_from_end(binary, 4)
        hex_result = ""
        result.reverse()
        for x in result:
            binary = x
            if len(binary) < 4:
                binary = binary.zfill(4)
            hex_result += table[binary]
        print("Result:", hex_result)
    bin_hex(number)


if system_first == 8 and system_second == 10:
    def oct_dec(number):
        dec = 0
        base = 1
        while number:
            last_digit = number % 10
            number = int(number / 10)
            dec += last_digit * base
            base = base * 8
        print("Result:", dec)
    oct_dec(number)


if system_first == 8 and system_second == 2:
    def oct_bin(number):
        num = ""
        while number != 0:
            d = int(number % 10)
            if d == 0:
                num = "".join(["000", num])
            elif d == 1:
                num = "".join(["001", num])
            elif d == 2:
                num = "".join(["010", num])
            elif d == 3:
                num = "".join(["011", num])
            elif d == 4:
                num = "".join(["100", num])
            elif d == 5:
                num = "".join(["101", num])
            elif d == 6:
                num = "".join(["110", num])
            elif d == 7:
                num = "".join(["111", num])
            number = int(number / 10)
        print("Result:", num)
    oct_bin(number)


if system_first == 8 and system_second == 16:
    def oct_hex(number):
        array = [str(i) for i in range(10)] + ["A", "B", "C", "D", "E", "F"]
        result = ""
        dec = 0
        base = 1
        while number:
            last_digit = number % 10
            number = int(number / 10)
            dec += last_digit * base
            base = base * 8
        while dec:
            result += array[dec % 16]
            dec //= 16
        print("Result:", result[::-1])
    oct_hex(number)


if system_first == 10 and system_second == 8:
    def dec_oct(number):
        octal = 0
        base = 0
        while number > 0:
            octal += ((number % 8) * (10 ** base))
            number = int(number / 8)
            base += 1
        print("Result:", octal)
    dec_oct(number)


if system_first == 10 and system_second == 2:
    def dec_bin(number):
        bin_num = 0
        power = 0
        while number > 0:
            bin_num += 10 ** power * (number % 2)
            number //= 2
            power += 1
        print("Result:", bin_num)
    dec_bin(number)


if system_first == 10 and system_second == 16:
    def dec_hex(number):
        array = [str(i) for i in range(10)] + ["A", "B", "C", "D", "E", "F"]
        res = ""
        while number:
            res += array[number % 16]
            number //= 16
        print("Result:", res[::-1])
    dec_hex(number)


if system_first == 16 and system_second == 8:
    def hex_oct(number):
        numb = (str(number))
        octal = ""
        dec = i = 0
        num = len(numb) - 1
        while i < len(numb):
            d = numb[i]
            if d == '0' or d == '1' or d == '2' or d == '3' or d == '4' or d == '5' or d == '6' or d == '7' or d == '8' or d == '9':
                dec = dec + int(d) * int(math.pow(16, num))
            elif d == 'A':
                dec = dec + 10 * int(math.pow(16, num))
            elif d == 'B':
                dec = dec + 11 * int(math.pow(16, num))
            elif d == 'C':
                dec = dec + 12 * int(math.pow(16, num))
            elif d == 'D':
                dec = dec + 13 * int(math.pow(16, num))
            elif d == 'E':
                dec = dec + 14 * int(math.pow(16, num))
            elif d == 'F':
                dec = dec + 15 * int(math.pow(16, num))
            i += 1
            num -= 1
        while dec > 0:
            octal = "".join([str(int(dec % 8)), octal])
            dec = int(dec / 8)
        print("Result:", octal)
    hex_oct(number)


if system_first == 16 and system_second == 10:
    def hex_dec(number):
        str_num = (str(number))
        num = 0
        str_num = str_num[::-1]
        power = 1
        for i in str_num:
            if i in "ABCDF":
                num += (ord(i) - ord('A') + 10) * power
            else:
                num += (ord(i) - ord('0')) * power
            power *= 16
        print("Result:", num)
    hex_dec(number)


def four_bin(str_number):
    return '0' * (4 - len(str_number)) + str_number


if system_first == 16 and system_second == 2:
    def hex_bin(number):
        str_number = (str(number))
        res = ''
        for i in str_number:
            if i.isdigit():
                binary = bin(int(i))[2:]
                res += four_bin(binary)
            elif i.isalpha() and ord(i) < 71:
                res += four_bin(bin(ord(i) - 55)[2:])
        print("Result:", res)
    hex_bin(number)
