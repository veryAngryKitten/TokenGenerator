import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%&*()")
hexdigits = list(string.hexdigits)
bindigits = [0,1]

print("TokenGenerator")

tokenGenChoose = input("HEX, bin, custom?(h/b/c)").lower()
length = int(input("Length: "))

def TokenGen(type, len):
    token = []

    if type.lower() == "h":
        for i in range(0, length):
            token.append(random.choice(hexdigits))
            
        for char in token:
            print(char, end="")

    if type.lower() == "b":
        for i in range(0, length):
            token.append(random.choice(bindigits))
            
        for char in token:
            print(char, end="")

    if type.lower() == "c":
        for i in range(0, length):
            token.append(random.choice(characters))
            
        for char in token:
            print(char, end="")

TokenGen(tokenGenChoose, length)