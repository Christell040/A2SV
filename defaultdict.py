from collections import defaultdict


n, m = map(int, input().split())


groupA = defaultdict(list)


for i in range(n):
    word = input()
    groupA[word].append(i + 1)  


for i in range(m):
    word = input()
    indices = groupA[word]
    
    if indices:
        print(" ".join(map(str, indices)))
    else:
        print(-1)
