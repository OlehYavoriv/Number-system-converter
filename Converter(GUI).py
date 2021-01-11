import math
from tkinter import *
from tkinter import messagebox
window = Tk()
window.maxsize(width="458", height="500")
window['bg'] = "#000000"
window.title = "Converter"
messagebox.showinfo("Information", "            Hello, User! \n"
                                               "This information will help you use the application\n"
                                               ">>Enter the number you want to convert using"
                                               " the keyboard in the number section.\n"
                                               ">>To clear the input window, click clear.\n"
                                               ">>Choose from which number system we translate your number.\n"
                                               ">>After that you will get the result.\n"
                                               ">>To exit the program, press exit.\n"
                                               "   P.s:If you enter a number from a computer keyboard,"
                                               " the letters should be uppercase.\n"
                                               "                             Good Luck!")

title = Label(window, text="Converter", font=('Arial', 18, 'bold'), fg='Yellow', bg='#000000')
title.pack(fill='x')
input_window = Entry(window, font=('Arial', 12), fg='white', bg='#1c1c1b', relief='sunken', bd=3)
input_window.pack(fill='x', pady=5)


def key(value):
    input_window.insert(END, value)


def clear():
    input_window.delete(0, END)
    display.configure(state='normal')
    display.delete(1.0, END)
    display.configure(state='disabled')


Num = LabelFrame(window, text='Number', fg='Yellow', bg='black')
Num.pack(fill='x', pady=5)
button15 = Button(Num, text='F', font=('Arial', 12), fg='Yellow', bg='Black', width=7, command=lambda: key('F'))
button15.grid(row=2, column=4)
button14 = Button(Num, text='E', font=('Arial', 12), fg='Yellow', bg='Black', width=7, command=lambda: key('E'))
button14.grid(row=1, column=4)
button13 = Button(Num, text='D', font=('Arial', 12), fg='Yellow', bg='Black', width=7, command=lambda: key('D'))
button13.grid(row=0, column=4)
button12 = Button(Num, text='C', font=('Arial', 12), fg='Yellow', bg='Black', width=7, command=lambda: key('C'))
button12.grid(row=2, column=3)
button11 = Button(Num, text='B', font=('Arial', 12), fg='Yellow', bg='Black', width=7, command=lambda: key('B'))
button11.grid(row=1, column=3)
button10 = Button(Num, text='A', font=('Arial', 12), fg='Yellow', bg='Black', width=7, command=lambda: key('A'))
button10.grid(row=0, column=3)
button7 = Button(Num, text='7', font=('Arial', 12), fg='Yellow', bg='Black', width=7, command=lambda: key(7))
button7.grid(row=0, column=0)
button8 = Button(Num, text='8', font=('Arial', 12), fg='Yellow', bg='Black', width=7, command=lambda: key(8))
button8.grid(row=0, column=1)
button9 = Button(Num, text='9', font=('Arial', 12), fg='Yellow', bg='Black', width=7, command=lambda: key(9))
button9.grid(row=0, column=2)
button4 = Button(Num, text='4', font=('Arial', 12), fg='Yellow', bg='Black', width=7, command=lambda: key(4))
button4.grid(row=1, column=0)
button5 = Button(Num, text='5', font=('Arial', 12), fg='Yellow', bg='Black', width=7, command=lambda: key(5))
button5.grid(row=1, column=1)
button6 = Button(Num, text='6', font=('Arial', 12), fg='Yellow', bg='Black', width=7, command=lambda: key(6))
button6.grid(row=1, column=2)
button1 = Button(Num, text='1', font=('Arial', 12), fg='Yellow', bg='Black', width=7, command=lambda: key(1))
button1.grid(row=2, column=0)
button2 = Button(Num, text='2', font=('Arial', 12), fg='Yellow', bg='Black', width=7, command=lambda: key(2))
button2.grid(row=2, column=1)
button3 = Button(Num, text='3', font=('Arial', 12), fg='Yellow', bg='Black', width=7, command=lambda: key(3))
button3.grid(row=2, column=2)
button0 = Button(Num, text='0', font=('Arial', 12), fg='Yellow', bg='Black', width=27, command=lambda: key(0))
button0.grid(row=3, column=0, columnspan=3)
button_clear = Button(Num, text='Clear', font=('Arial', 12), fg='Yellow', bg='Black', width=17, command=clear)
button_clear.grid(row=3, column=3, columnspan=2)


def chunk_str_from_end(string, chunk_size):
    result = []
    i = len(string)
    while i > 0:
        if i - chunk_size > 0:
            result.append(string[i - chunk_size:i])
        else:
            result.append(string[0:i])
        i -= chunk_size
    return result


table = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6',
              '0111': '7', '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D',
              '1110': 'E', '1111': 'F'}


def bin_hex(binary):
    chunk_result = chunk_str_from_end(binary, 4)
    hex_result = ""
    chunk_result.reverse()
    for x in chunk_result:
        binary_chunk = x
        if len(binary_chunk) < 4:
            binary_chunk = binary_chunk.zfill(4)
        hex_result += table[binary_chunk]
    return hex_result


def bin_dec(value):
 dec_num = 0
 power = 0
 while value > 0:
  dec_num += 2 ** power * (value % 10)
  value //= 10
  power += 1
 return dec_num


def bin_oct(value):
 octal = 0
 decimal = 0
 i = 0
 while value != 0:
  decimal += int((value % 10) * math.pow(2,i))
  i = i + 1
  value = int(value/10)
 i = 1
 while decimal != 0:
  octal += (decimal % 8) * i
  decimal = int(decimal/8)
  i *= 10
 return octal
 return decimal


def binary():
    display.configure(state='normal')
    display.delete(1.0, END)
    try:
        value = int(input_window.get())
        binary = str(input_window.get())
        display.insert(END, 'Oct  =  ' + str(bin_oct(value)))
        display.insert(END, '\nDec  =  ' + str(bin_dec(value)))
        display.insert(END, '\nHex =  ' + str(bin_hex(binary)))
    except:
        display.insert(END, 'Wrong!')
    display.configure(state='disabled')


def oct_dec(value):
    dec = 0
    base = 1
    while value:
        last_digit = value % 10
        value = int(value / 10)
        dec += last_digit * base
        base = base * 8
    return dec


def oct_bin(value):
    num = ""
    while value != 0:
        d = int(value % 10)
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
        value = int(value / 10)
    return num


def oct_hex(value):
    array = [str(i) for i in range(10)] + ["A", "B", "C", "D", "E", "F"]
    result = ""
    dec = 0
    base = 1
    while value:
        last_digit = value % 10
        value = int(value / 10)
        dec += last_digit * base
        base = base * 8
    while dec:
            result += array[dec % 16]
            dec //= 16
    return result[::-1]


def octal():
    display.configure(state='normal')
    display.delete(1.0, END)
    try:
        value = int(input_window.get())
        display.insert(END, 'Bin   =  ' + str(oct_bin(value))[1:])
        display.insert(END, '\nDec  =  ' + str(oct_dec(value)))
        display.insert(END, '\nHex = ' + str(oct_hex(value)))
    except:
        display.insert(END, 'Wrong!')
    display.configure(state='disabled')


def dec_oct(value):
 octal = 0
 ctr = 0
 while value > 0:
    octal += ((value % 8) * (10 ** ctr))
    value = int(value / 8)
    ctr += 1
 return octal


def dec_bin(value):
    bin_num = 0
    power = 0
    while value > 0:
        bin_num += 10 ** power * (value % 2)
        value //= 2
        power += 1
    return bin_num


def dec_hex(value):
    array = [str(i) for i in range(10)] + ["A", "B", "C", "D", "E", "F"]
    res = ""
    while value:
        res += array[value % 16]
        value //= 16
    return res[::-1]


def decimal():
    display.configure(state='normal')
    display.delete(1.0, END)
    try:
        value = int(input_window.get())

        display.insert(END, 'Bin  =  ' + str(dec_bin(value)))
        display.insert(END, '\nOct    =  ' + str(dec_oct(value)))
        display.insert(END, '\nHex = ' + str(dec_hex(value)))
    except:
        display.insert(END, 'Wrong!')
    display.configure(state='disabled')


def four_bin(value):
    return '0' * (4 - len(value)) + value


def hex_bin(value):
    res = ''
    for i in value:
        if i.isdigit():
            binary = bin(int(i))[2:]
            res += four_bin(binary)
        elif i.isalpha() and ord(i) < 71:
            res += four_bin(bin(ord(i) - 55)[2:])
    return res


def hex_oct(value):
 octal = ""
 dec = i = 0
 num = len(value) - 1
 while i < len(value):
    d = value[i]
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
 return octal


def hex_dec(value):
    num = 0
    value = value[::-1]
    power = 1
    for i in value:
        if i in "ABCDF":
            num += (ord(i) - ord('A')+10)*power
        else:
            num += (ord(i) - ord('0')) * power
        power *= 16
    return num


def hexadecimal():
    display.configure(state='normal')
    display.delete(1.0, END)
    try:
        value = str(input_window.get())
        display.insert(END, 'Bin   =  ' + str(hex_bin(value))[2:])
        display.insert(END, '\nOct   =  ' + str(hex_oct(value)))
        display.insert(END, '\nDec = ' + str(hex_dec(value)))
    except:
        display.insert(END, 'Wrong!')
    display.configure(state='disabled')


button = LabelFrame(window, text="From which number system do we convert", bg='black', fg='yellow')
button.pack(fill='both', pady=5)
binButton = Button(button, text="Bin", font=('Arial', 12), fg='Yellow', bg='black', width=9, command=binary)
binButton.grid(row=0, column=0)
octButton = Button(button, text="Oct", font=('Arial', 12), fg='Yellow', bg='black', width=9, command=octal)
octButton.grid(row=0, column=1)
decButton = Button(button, text="Dec", font=('Arial', 12), fg='Yellow', bg='black', width=10, command=decimal)
decButton.grid(row=0, column=2)
hexButton = Button(button, text="Hex", font=('Arial', 12), fg='Yellow', bg='black', width=10, command=hexadecimal)
hexButton.grid(row=0, column=3)
button_exit = Button(button, text='Exit', font=('Arial', 12), fg='Yellow', bg='black', width=20, command=window.destroy)
button_exit.grid(row=1, column=1, columnspan=2)

display = Text(window, font=('Arial', 12), fg='white', bg='#1c1c1b', relief='sunken', bd=3)
display.pack(fill='x')
display.configure(state='disabled')

window.mainloop()
