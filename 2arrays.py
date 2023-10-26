test_cases = int(input())

for _ in range(test_cases):
    num_elements = int(input())
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))
    is_possible = True
    list_a.sort()
    list_b.sort()
    
    for i in range(num_elements):
        if list_a[i] != list_b[i] and list_a[i] + 1 != list_b[i]:
            is_possible = False

    if is_possible:
        print("YES")
    else:
        print("NO")
