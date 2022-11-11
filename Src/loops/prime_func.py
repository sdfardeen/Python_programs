def prime_number(start, end):
    for i in range(start, end):
        # print(is_prime_number(i))
        if is_prime_number(i):
            print(i)


def is_prime_number(n):
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True


prime_number(start=8, end=70)
print(is_prime_number(2))
