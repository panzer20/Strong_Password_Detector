#!/usr/bin/env python3

import re

def is_strong_password():
    password = input("Enter a password: ")
    matchObject = re.search(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$', password)
    if not matchObject:
        print("Password isn't strong.")
    else:
        print("Password is strong.")

is_strong_password()