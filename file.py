"""# method 1 : Here, we need to manually close the file after the operation
# ****************** Writing File ******************
fp = open("my_file.txt", "w")  # Writing to a file
writing_file = fp.write("Hello World\n How are you doing?")  # write() : it writes the passed content to the file
print("Number of characters written = ", writing_file)
fp.close()

# ****************** Reading File ******************
fp = open("my_file.txt", 'r')  # Reading a file
# open("File path name", "Mode = r,w,a,r+,x..")
print("\nread() = ", fp.read())  # read() : it returns whole content of the file
fp.seek(0)  # seek(position_of_character) : it sets the file pointer at the top
print("\nreadline() = ", fp.readline())  # readline() : it returns single line
fp.seek(0)
print("\nreadlines() = ", fp.readlines())  # readline() : it returns all the lines in the list format
fp.close()  # close() : it close the file

# ****************** Appending File ******************
fp = open("my_file.txt", "a")  # mode='a' : To Appending data to a file
appending_file = fp.write("\nHope you are doing well.")  # write() : it writes the passed content to the file
print("\nNumber of characters appended = ", appending_file)
fp.close()

# ****************** Reading File ******************
fp = open("my_file.txt", 'r')  # Reading a file
# open("File path name", "Mode = r,w,a,r+..")
print("\nread() = ", fp.read())  # read() : it returns whole content of the file
fp.seek(0)  # seek(position_of_character) : it sets the file pointer at the top
print("\nreadline() = ", fp.readline())  # readline() : it returns single line
fp.seek(0)
print("\nreadlines() = ", fp.readlines())  # readline() : it returns all the lines in the list format
fp.close()  # close() : it close the file"""

# method 2 : Here, automatically file will be closed
# ****************** Writing File ******************
with open("my_file.txt", 'w') as fp:
    writing_file = fp.write("Hello World\n How are you doing?")  # write() : it writes the passed content to the file
    print("Number of characters written = ", writing_file)

# ****************** Reading File ******************
with open("my_file.txt", 'r') as fp:
    print("\nread() = ", fp.read())  # read() : it returns whole content of the file
    fp.seek(0)  # seek(position_of_character) : it sets the file pointer at the top
    print("\nreadline() = ", fp.readline())  # readline() : it returns single line
    fp.seek(0)
    print("\nreadlines() = ", fp.readlines())  # readline() : it returns all the lines in the list format
    fp.close()  # close() : it close the file

# ****************** Appending File ******************
with open("my_file.txt", 'a') as fp:  # mode='a' : To Appending data to a file
    appending_file = fp.write("\nHope you are doing well.")  # write() : it writes the passed content to the file
    print("\nNumber of characters appended = ", appending_file)

# ****************** Reading File ******************
with open("my_file.txt", 'r') as fp:
    print("\nread() = ", fp.read())  # read() : it returns whole content of the file
    fp.seek(0)  # seek(position_of_character) : it sets the file pointer at the top
    print("\nreadline() = ", fp.readline())  # readline() : it returns single line
    fp.seek(0)
    print("\nreadlines() = ", fp.readlines())  # readline() : it returns all the lines in the list format
    fp.close()  # close() : it close the file
