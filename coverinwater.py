for i in range(int(input())):
    x = input()
    y = input()


    def find(s):
        count = 0
        cur = 0
        for i in range(len(s)):
            if s[i] == ".":
                cur+=1
                count = max(count,cur)
            else:
                cur = 0
        return count >= 3
    
    def count(s):
        count = 0
        for i in range(len(s)):
            if s[i] == ".":
                count+=1
        return count
    
    if find(y):
        print(2)
    else:
        print(count(y))

  


