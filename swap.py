#!/usr/bin/python3

def swap_case(s):
    for x in s:
        if x.isupper():
            print(x.lower(), end="")
        else:
            print(x.upper(), end="")
    print("\n")
s = input("Enter any string:\n>> ")
swap_case(s)