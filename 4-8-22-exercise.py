# Exercise!
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

for i in range(len(picture)):
    for j in range(len(picture[i])):
        if picture[i][j]:
            print("*", end='')
        else:
            print(" ", end='')
    print("\n")

for row in picture:
    for pixel in row:
        if pixel:
            print("*", end='')
        else:
            print(" ", end='')
    print("")

for row in picture:
    for pixel in row:
        print("*", end='') if pixel else print(" ", end='')
    print('')
