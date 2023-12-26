# author: Andrew Yniguez
# date: Nov 29, 2020
# file: cipher.py is a program that can encode or decode messages from files in the same directory as the program.
#       First it asks for an action, then asks for a file to read from and a file to write result to.

import os

# check if filename is a regular, readable, file in the current directory
def is_file_r_accessible(file_path):
    # check if the file exists
    if os.path.exists(file_path):
        # check if the file is not a directory
        if os.path.isfile(file_path):
            # check if the file is readable
            if os.access(file_path, os.R_OK):
                return True
            else:
                print("")
                print(f"The file '{file_path}' is not readable.")
                print("")
        else:
            print("")
            print(f"'{file_path}' is not a regular file.")
            print("")
    else:
        print("")
        print(f"The file '{file_path}' does not exist.")
        print("")
    
    return False

# check if filename is a regular, writable, file in the current directory
def is_file_w_accessible(file_path):
    # check if the file exists
    if os.path.exists(file_path):
        # check if the file is not a directory
        if os.path.isfile(file_path):
            # check if the file is writadable
            if os.access(file_path, os.W_OK):
                return True
            else:
                print("")
                print(f"The file '{file_path}' is not writable.")
                print("")
        else:
            print("")
            print(f"'{file_path}' is not a regular file.")
            print("")
    else:
        print("")
        print(f"The file '{file_path}' does not exist.")
        print("")
    
    return False

# read text from a file and return text as a string
def readfile(filename):
    #open file
    readf = open(filename, "r")
    # reads file content and prints in upper case
    read = (readf.read())
    return read.upper()
    # closes file
    readf.close()

# write a string (message) to a file
def writefile(filename, text):
    # open file
    writef = open(filename, "w")
    # writes content in, closes it
    writef.write(text)
    writef.close()

# make a list (tuple) of letters in the English alphabet
def make_alphabet():
    alphabet = ()
    for i in range(26):
        char = i + 65
        alphabet += (chr(char),)
    #print (alphabet)
    return alphabet

# encode text letter by letter using a Caesar cipher
# return a list of encoded symbols
def encode(plaintext):
    plaintext = plaintext.upper()
    shift = 3
    ciphertext = []
    alphabet = make_alphabet()
    length = len(alphabet)
    for char in plaintext:
        found = False
        for i in range(length):
            if char == alphabet[i]:
                letter = alphabet[(i + shift) % length]
                ciphertext.append(letter)
                found = True
                break
        if not found:
            ciphertext.append(char)
    return ciphertext
    

# decode text letter by letter using a Caesar cipher
# return a list of decoded symbols
# check how the function encode() is implemented
# your implementation of the function decode() can be very similar
# to the implementation of the function encode()
def decode(ciphertext):
    # same stuff as the encode function, just with the variables changed a bit
    ciphertext = ciphertext.upper()
    shift = -3
    plaintext = []
    alphabet = make_alphabet()
    length = len(alphabet)
    for char in ciphertext:
        found = False
        for i in range(length):
            if char == alphabet[i]:
                letter = alphabet[(i + shift) % length]
                plaintext.append(letter)
                found = True
                break
        if not found:
            plaintext.append(char)
    return plaintext


# convert a list into a string
def to_string(text):
    s = ""
    # adds up all the items in the list to turn them into a string
    for i in text:
        s += i
    return s

# main program
# will keep the program on a loop
cont = True
opt = " "

while cont == True:
    # get inputs for using the program
    print("Would you like to encode or decode the message?")
    opt = input("Type 'e' to encode, 'd' to decode, or 'q' to quit: ")
    if opt != "e" and opt != "d" and opt != "q":
        print("")
        print(opt, "is not a valid option.")
        print("")
        continue 
    # if quit game then exit loop
    if opt == "q":
        break
    
    rfile = input("Please enter a file for reading: ")
    while is_file_r_accessible(rfile) == False:
        rfile = input("Retry. Please enter a file for reading: ")

    wfile = input("Please enter a file for writing: ")
    while is_file_w_accessible(rfile) == False:
        wfile = input("Retry. Please enter a file for writing: ")

    print("")

    # elif for whether its decoding or encoding
    if opt == "e":
        # print messages
        print("Plaintext: ")
        # calls on read function
        readfile(rfile)
        # emessage = text read from file, prints it
        emessage = readfile(rfile)
        print(emessage)
        print("")
        
        print("Ciphertext: ")
        # endodes content
        encode(emessage)
        # turns encoded list into encoded message
        to_string(encode(emessage))
        # ciphertext = encoded message
        ciphertext = to_string(encode(emessage))
        # prints ciphertext
        print(ciphertext)
        print("")
        # calls on write function
        writefile(wfile, ciphertext)
        
    elif opt == "d":
        # print messages
        print("Ciphertext: ")
        # calls on read function
        readfile(rfile)
        # dmessage = text read from file, prints it
        dmessage = readfile(rfile)
        print(dmessage)
        print("")

        print("Plaintext: ")
        # calls on decode function
        decode(dmessage)
        to_string(decode(dmessage))
        # plaintext = decoded message
        plaintext = to_string(decode(dmessage))
        # prints plaintext and closes read file
        print(plaintext)
        print("")
        # calls on write function
        writefile(wfile, plaintext)
        
# ends the program
print("")  
print("Goodbye!")
