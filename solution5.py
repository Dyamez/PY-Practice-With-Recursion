# Write code for algorithm 5 below
def isa_palindrome(str):
    if len(str) == 1 or len(str) == 0:
        return True
    return (str[0] == str[-1]) and isa_palindrome(str[1:-1])


print(f'is apple a palindrom? {isa_palindrome("apple")}')
print(f'is tacoCat a palindrom? {isa_palindrome("tacoCat")}')

print(f'is avocado a palindrom? {isa_palindrome("avocado")}')
