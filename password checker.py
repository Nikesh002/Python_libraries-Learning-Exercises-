# At least 8 char long
# contain any sort letters, numbers $%#@
# should end with a digit

import re

pattern = re.compile(r"[a-zA-Z0-9$%#@]{8,}\d")
password = str(input(" Please enter a password = "))

a = pattern.fullmatch(password)
if a is None:
    print(" Invalid password !!! ")
else:
    print(" Welcome !!! ")
