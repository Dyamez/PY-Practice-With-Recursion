# Write code for algorithm 2 below
def natural_numbers(n, i=1):
    if i > n:
        return
    else:
        print(i)
        natural_numbers(n, i + 1)


natural_numbers(996)
