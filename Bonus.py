def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


print(f"the gcd of 15 and 10: {gcd(15, 10)}")
