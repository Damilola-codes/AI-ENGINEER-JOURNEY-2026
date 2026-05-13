#!/usr/bin/env python3

for x in range(1, 101):
    if (x % 3 == 0) and (x % 5 == 0):
        print('DataModel', sep=', ')
    elif (x == 3) or (x % 3 == 0):
        print('Data', sep=', ')
    elif (x == 5) or (x % 5 == 0):
        print('Model', sep=', ')
    else:
        print(x, sep=', ')

