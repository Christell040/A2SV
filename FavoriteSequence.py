t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))

    a = [0] * n
    left = 0
    right = n - 1
    value = 1

    for i in range(n):
        if i % 2 == 0:
            a[i] = b[left]
            left += 1
        else:
            a[i] = b[right]
            right -= 1

    print(*a)
