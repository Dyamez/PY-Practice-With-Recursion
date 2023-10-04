def name_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


name_args(dyamez="lame", ham="delicious", today="my birthday")


def all_true(*args):
    return all(args)


print(all_true(True, False, False))


def one_true(*args):
    return any(args)


print('one_true', one_true(1, 0, 0))
print('one_true', one_true(0, False, 0))


def recursive_factorial(n):
    if n <= 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)


print('recursive factorial of 6 is', recursive_factorial(6))


def recur_dedup(my_str, i=0):
    print('recurs_dedup progress', my_str, i)
    if len(my_str) <= 1 or i == len(my_str) - 1:
        return my_str
    else:
        if my_str[i] == my_str[i + 1]:
            return recur_dedup(my_str[0:i] + my_str[i + 1:], i)
        else:
            return recur_dedup(my_str, i + 1)


print(recur_dedup('apple'))
print(recur_dedup('AABBCCDD'))


def recurse_reverse(str, i=0):
    if len(str) == 0:
        return ''
    elif i == len(str) - 1:
        return str[0]
    else:
        return str[-1 - i] + recurse_reverse(str, i + 1)


print(recurse_reverse('racecar'))
print(recurse_reverse('You rule!'))
