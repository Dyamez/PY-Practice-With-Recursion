# Write code for algorithm 3 below
def nth_fib(n):
    if n <= 0:
        print('Nope!')
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return nth_fib(n - 1) + nth_fib(n - 2)


print(f'2nd fib number is {nth_fib(2)}')

print(f'the 6th fib number is {nth_fib(6)}')
print(f'the 7th fib number is {nth_fib(7)}')
print(f'the 8th fib number is {nth_fib(8)}')
print(f'the 9th fib number is {nth_fib(9)}')

print(f'the 20th fib number is {nth_fib(20)}')
