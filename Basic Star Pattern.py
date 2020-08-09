pattern = [[0, 0, 0, 1, 0, 0, 0],
           [0, 0, 1, 1, 1, 0, 0],
           [0, 1, 1, 1, 1, 1, 0],
           [1, 1, 1, 1, 1, 1, 1],
           [0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0]]
for row in pattern:
    for element in row:
        if element:
            print("*", end='')
        else:
            print(" ", end='')
    print()
