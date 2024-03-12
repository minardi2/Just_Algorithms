
def factorial_rec(x):
    """recursive function"""

    if x == 1:
        return 1
    else:
        return (x * factorial_rec(x-1))

num = 10
print("The factorial of", num, "is", factorial_rec(num))


def factorial_non_rec(n):
    """non recursive function"""

    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

print("The factorial of", num, "is", factorial_non_rec(num))
