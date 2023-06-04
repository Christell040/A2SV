A = set(map(int, input().split()))  # Set A
n = int(input())  # Number of other sets

is_superset = True

for _ in range(n):
    other_set = set(map(int, input().split()))  # Get the other set

    if not A.issuperset(other_set):
        is_superset = False
        break

print(is_superset)