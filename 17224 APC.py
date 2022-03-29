N, L, K = map(int, input().split())

easy, hard = 0, 0

for i in range(N):
  sub1, sub2 = map(int, input().split())
  if sub2 <= L:
    hard += 1
  elif sub1 <= L:
    easy += 1

// 풀 수 있는 어려운 문제의 수만큼 먼저 계산해준다. 
   K 문제 이하로 풀어야 하므로 min()을 사용해준다.//
ans = min(hard, K) * 140


//아직 K 문제만큼 풀지 못 했을 경우 K 문제에서 풀어낸 
  어려운 문제의 개수를 뺀 값과 풀어낸 쉬운 문제의 수의 min 만큼 계산해준다. //
if hard < K:
  ans += min(K-hard, easy) *100

print(ans)