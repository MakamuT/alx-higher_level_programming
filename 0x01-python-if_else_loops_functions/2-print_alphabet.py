#!/usr/bin/python3
# prints the  ASCII alphabet in lowercase
# ASCII code of the character codes for 'a' and 'z' is between 97 and 122

for alphaletters in range(97, 123):
    print("{}".format(chr(alphaletters)), end = "")
