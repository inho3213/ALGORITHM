#부분수열의 합
from itertools import combinations

N, S = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0

for i in range(1, N+1):
  a = list(combinations(nums, i))

  for j in a:
    if sum(j) == S:
      cnt += 1

print(cnt)