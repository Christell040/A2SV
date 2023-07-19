n = int(input())
skills = list(map(int, input().split()))

skills.sort()

team_size = 0
left = 0
right = 0

while right < n:
    if skills[right] - skills[left] <= 5:
        team_size = max(team_size, right - left + 1)
        right += 1
    else:
        left += 1

print(team_size)