with open('file.xml', mode="r") as my_file:
    text = my_file.readlines()
    print(text)
    with open('newfile.xml', mode='w') as my_file2:
        for string in text:
            my_file2.write(string[0:-1].strip())
