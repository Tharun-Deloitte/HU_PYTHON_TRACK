nrow = int(input('enter number of row: '))

#up
for row in range(1, nrow + 1):
    for col in range(1, nrow - row + 1):
        print(" ", end="")
    for col in range(1, 2 * row):
        print("*", end="")
    print()

#down
for row in range(nrow - 1, 0, -1):
    for col in range(1, nrow - row + 1):
        print(" ", end="")
    for col in range(1, 2 * row):
        print("*", end="")
    print()