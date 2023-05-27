def is_prime(n):
    if not n <= 2:
        for i in range(2, n):
            if n % i == 0:
                return False
                break
    elif n == 1:
        return False
    elif n == 2:
        return True
    elif n == 0:
        return False

    return True


def prime_counter(n):
    count = 0
    for i in range(0, n):
        if is_prime(i):
            count += 1
    return count

print(prime_counter(10))