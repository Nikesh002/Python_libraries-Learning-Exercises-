str1 = "welcome"
# capitalize()
print(str1.capitalize())

# Upper()
print(str1.upper())

# Lower()
print(str1.lower())

# isalpha() : check if the string contains alphabets only
print(str1.isalpha())

str2 = '88'
# isnumeric : to check if the string is numeric digits
print(str2.isnumeric())

str3 = 'Pop is a good guy'
print(str3.startswith('Pop'))
print(str3.endswith('guy'))
print(str3.replace('Pop',
                   'Mini'))  # replace('source_str','destination_str') : Replace the source string with the destination string
print(str3.find('good'))  # find('str') : it returns index of searched string
print()

str4 = '     Hello     '
print("str4 = ", str4)
print("str4.lstrip() =", str4.lstrip())  # remove the left side blank spaces
print("str4.rstrip() =", str4.rstrip())  # remove the right side blank spaces
print("str4.strip() =", str4.strip())  # remove the both sides blank spaces
print()

print("str3 = ", str3)
print(str3.split(' '))  # it returns the list of sub-strings separated by mentioned delimiter
print(str3.splitlines())  # it returns whole line of string in a list
print()

a = 'Mike', 'Nike'
print(a)
b = ','
print(b.join(a))
print()

# String formatting
fname = 'Mike'
lname = 'Rose'
print("Hey {}, your last name is {}. right?".format(fname, lname))
print()

price = 127
with_tax = price * 18 / 100
print("Price = Rs{:.2f}. With tax = Rs{:.2f}".format(price, with_tax))
