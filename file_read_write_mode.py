with open("my_file1.txt", 'w') as fp: # here, we are creating new file which is not already exist. Refer following url to uderstand for different modes = https://www.programiz.com/python-programming/methods/built-in/open
    pass

with open("my_file1.txt", 'r+') as fp:  # 'r+' : Read/Write mode
    wf = fp.write("Hello world,\n How are you?")  # Writing data to the file
    print(wf)  # Print number of writen characters
    fp.seek(0)  # seek(position_of_character) : it sets the file pointer at the top
    rf = fp.read()  # Reading data from the file
    print(rf)  # Print content of the file
