# *args & **kwargs
# Function passing parameters order Rule : params, *args, default params, **kwargs

def args_kwargs(*args, **kwargs):
    print(args)
    print(args[2])
    print(kwargs)
    print(kwargs.values())
    for k in kwargs.keys():
        if k == 'a1':
            print(" Value of a1 is ",kwargs[k])
    return


args_kwargs(1, 2, "Sam", 3, a1="Hi", a2="There")
