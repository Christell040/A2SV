# Enter your code here. Read input from STDIN. Print output to STDOUT

English = int(input())
english_list = set(map(int, input().split()))

Fremch = int(input())
French_list = set(map(int, input().split()))

difference = english_list - French_list

print(len(difference))
