# Characters & Character Sequences

# ^ - Matches the beginning of a line : e.g. pattern="^It"
# $ - Matches the end of a line : e.g. pattern="g$"
# . - Matches any character : e.g. pattern="^I..."
# \d - Matches any digit : e.g. pattern="\d"
# \D - Matches any non-digit : e.g. pattern="\D"
# \s - Matches whitespace : e.g. pattern="\s"
# \S - Matches any non-whitespace : e.g. pattern="\S"

import re

str1 = "It is a dog 56"
pattern1 = "\S"
print(re.findall(pattern1, str1, flags=0), end="\n\n")

# * - Repeats a character zero or more times : e.g. pattern="ma*"
# + - Repeats a character one or more times : e.g. pattern="a+"
# ( - Indicates where string starting extraction is to start : e.g. pattern="^From (\S*@\S*)"
# ) - Indicates where string starting extraction is to end : e.g. pattern="^From (\S*@\S*)"
# ? - Matches the expression 0 to 1 times : e.g. pattern="^F.*?"

str2 = "From booby.mark@gmail.com"
pattern2 = r"[a-z0-9]+[-.]*[a-z0-9]+@[a-z]+\.[a-z]+"
print(re.findall(pattern2, str2),end="\n\n")

# []
# [aeiou] - Matches a single character in the listed set
# [^xyz] - Matches a single character : it prints all the characters except the characters mentioned in the pattern
# [a-z 0-9] - Set of characters can include a range
# {} : it helps us to know number of characters are present in the string : e.g. pattern = "n{2}"

str3 = "pythonn"
pattern3 = "n{2}"
print(re.findall(pattern3,str3,flags=0),end="\n\n")

# Task
print(str2)
pattern4 =r"@([^ ]*)"
print(re.findall(pattern4,str2,flags=0),end="\n\n")
