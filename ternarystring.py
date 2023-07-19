t = int(input())

for _ in range(t):
    s = input()

    counter = {1: 0, 2: 0, 3: 0}
    distinct_chars = 0
    min_length = float('inf')

    left = 0
    right = 0

    while right < len(s):
        counter[int(s[right])] += 1

        if counter[int(s[right])] == 1:
            distinct_chars += 1

        if distinct_chars == 3:
            while counter[int(s[left])] > 1:
                counter[int(s[left])] -= 1
                left += 1

            min_length = min(min_length, right - left + 1)

        right += 1

    if min_length == float('inf'):
        print(0)
    else:
        print(min_length)
