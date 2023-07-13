# Syntax error
"""a = 5
if not a:
    print("False")
else
    print("True")
***************
  File "E:\Python\Projects\Tutedude\errors.py", line 5
    else
        ^
SyntaxError: expected ':'"""

# Indentation error
"""if True:
print("False")
***************
File "E:\Python\Projects\Tutedude\errors.py", line 15
    print("False")
    ^
IndentationError: expected an indented block after 'if' statement on line 14
"""

# Zero Division error
"""print(0/0)
***************
File "E:\Python\Projects\Tutedude\errors.py", line 24, in <module>
    print(0/0)
          ~^~
ZeroDivisionError: division by zero"""

# Module error

"""import mathematics
print(mathematics.pi)
***************
File "E:\Python\Projects\Tutedude\errors.py", line 33, in <module>
    import mathematics
ModuleNotFoundError: No module named 'mathematics'"""

# Type error

"""print(5+'5')
***************
File "E:\Python\Projects\Tutedude\errors.py", line 42, in <module>
    print(5+'5')
          ~^~~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'"""