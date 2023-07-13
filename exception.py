try:  # This block is going to throw the error
    a = 2
    b = 5
    print(a / b)
except ZeroDivisionError:  # Here we are catching the expected exceptions
    print(" Zero Division error. ")
finally:  # Whatever may be the exception this code is going to be executed at the end
    print("Continue with the following code.")
