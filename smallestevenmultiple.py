import math

def smallest_multiple(n):
    return (2 * n) // math.gcd(2, n)

# Example usage
n = 5
result = smallest_multiple(n)
print(result)  # Output: 10

n = 6
result = smallest_multiple(n)
print(result)  # Output: 6
