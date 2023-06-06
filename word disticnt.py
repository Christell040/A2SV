from collections import OrderedDict

n = int(input())
words = []


for i in range(n):
    word = input().rstrip()
    words.append(word)


word_counts = OrderedDict()
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1


distinct_words = len(word_counts)
occurrences = list(word_counts.values())

print(distinct_words)
print(*occurrences)
