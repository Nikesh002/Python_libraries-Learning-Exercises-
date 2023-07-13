# **** Session 1 ****
# my_file = open('test.txt')
# print(my_file.read())
# my_file.seek(0)
# print(my_file.readline())
# my_file.seek(0)
# print(my_file.readlines())
# my_file.close()

# **** Session 2 ****
# Read + Write mode
with open('test.txt', mode='r+') as my_file:
    text = my_file.write(' Hey it\'s me..')
    print(my_file.read())

# Append mode & it creates a new file if the given file name doesn't exist.
with open('test.txt', mode='a') as my_file:
    text = my_file.write(' :) ')
    print(text)

# Write only mode & it overwrites the content of the existing file
# & it creates a new file if the given file name doesn't exist.
with open('test.txt', mode='w') as my_file:
    text = my_file.write(' :) ')
    print(text)

# Read the file content
with open('test.txt', mode='r') as my_file:
    print(my_file.read())