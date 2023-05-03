#로또 
#조합 라이브러리 사용하기

from itertools import combinations

while True:
  nums = list(map(int, input().split()))
  k = nums[0]
  S = nums[1:]

  lotto = list(combinations(S, 6))
  for i in lotto:
    print(*i)
    #앞에 *붙이면 괄호 없이 한번에 출력가능
  print()
  
  #입력 마지막에는 0
  if k == 0:
    break