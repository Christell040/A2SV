

for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))


    def res(arr):
        index = n-2
        for i in range(n-1):
            if arr[i] != 0:
                index = i
                break
        return sum(arr[index:]) + arr[index+1:].count(0)


    print(res(arr[0:n-1]))
