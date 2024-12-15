def pc(a, b, c, d):
    if a == 'x':
        print((c * b) / d)
    elif b == 'x':
        print((a * d) / c)
    elif c == 'x':
        print((a * d) / b)
    elif d == 'x':
        print((b * c) / a)
    else:
        print("Error: One value must be 'x'.")

pc(1, 2, 2, 'x') 