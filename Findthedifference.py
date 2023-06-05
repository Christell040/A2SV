original = input()
shuffled = input()

maximum = max(original,shuffled)

indicator =True
storer = ''
for i in shuffled:
    if i in original:
        continue
    else: 
        storer += i
print(storer)
