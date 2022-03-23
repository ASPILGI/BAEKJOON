t = int(input())

for _ in range(t):
  n = int(input())
  coins = [25, 10, 5, 1]
  ans = []
  for i in range(4):
    ans.append(n//coins[i])
    n %= coins[i]
  print(*ans)