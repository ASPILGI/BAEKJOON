n = int(input())

a = list(map(int, input().split(' ')))

max_a = max(a)

print(sum(a) - max_a)