from translate import Translator

translator = Translator(to_lang="ja")

try:
    with open("E:\Python\Projects\ZTM\\translator\\text.txt", mode="r") as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
        with open("E:\Python\Projects\ZTM\\translator\\text-ja.txt", mode="w", encoding="utf-8") as my_file2:
            my_file2.write(translation)
except FileNotFoundError as err:
    print(" File not Found. ")
    err
except IOError as err:
    print(" IO Error. ")
    err

# try:
#     with open("E:\Python\Projects\ZTM\\translator\\text.txt", mode="r") as my_file:
#         my_file.seek(0)
#         lines = len(my_file.readlines())
#         my_file.seek(0)
#         for x in range(lines):
#             text = my_file.readline()
#             translation = translator.translate(text)
#             print(translation)
# except FileNotFoundError as err:
#     print(" File not Found. ")
#     err
# except IOError as err:
#     print(" IO Error. ")
#     err
