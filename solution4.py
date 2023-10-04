def power(a, b):
    if b < 1:
        print('Nope!')
    elif b == 1:
        return a
    else:
        return a * power(a, b - 1)


print(power(2, 4))
print(power(10, 10))
