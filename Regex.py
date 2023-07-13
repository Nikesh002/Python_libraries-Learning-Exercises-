# Regular expressions
# regex
# mostly applied on Strings
# Module name : import re
# Used to validate the pattern

# 1 : match(pattern,string,flags) : it compares the first set of characters in the given input string with the pattern
# Here, it tries to match starting part of the input string to the pattern
import re

pattern = "king"
res = re.match(pattern, "fkingOfTheWorld")
print(bool(res), end="\n\n")

# 2 : findall(pattern,string,flags) : it returns list of all the matches patterns in the given string at any positions.
str1 = re.findall(pattern, "akingskings")
print(str1, end="\n\n")

# 3 : search(pattern,string,flags) : Here, it returns True if the pattern occurs in the given string else returns False

str2 = re.search(pattern, "saskingking", flags=0)
print(bool(str2), end="\n\n")

# 4 : sub(pattern,replace_chars,string,count,flags) : Here, we are replacing the "cat" if we find the pattern(i.e."dog")
# in the given string

str3 = "It is a dog"
pattern1 = "dog"
print(re.sub(pattern1,"cat",str3,count=0,flags=0))
