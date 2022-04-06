nrows= int(input('enter number of rows:'))

for row in range(nrows):
    for col in range(nrows - row):
        print(' ', end='')  # printing space required and staying in same line

    for col in range(2 * row + 1):
        if col == 0 or col == 2 * row or row == nrows - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()