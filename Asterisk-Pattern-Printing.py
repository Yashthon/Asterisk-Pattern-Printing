def pattern(a, c):
    if c == True:
        i = 0
        while i < a:
            print(" * " * (i + 1))
            i = i + 1
    elif c == False:
        i = a
        while i > 0:
            print(" * " * i)
            i = i - 1


a = int(input('Enter no. of rows:\n'))
b = int(input('0 or 1?\n'))
c = bool(b)
pattern(a, c)
