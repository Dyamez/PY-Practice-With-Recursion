# Write code for algorithm 1 below
def count_down(num):
    if (num == 0):
        return
    else:
        print(num)
        count_down(num - 1)


count_down(20)
