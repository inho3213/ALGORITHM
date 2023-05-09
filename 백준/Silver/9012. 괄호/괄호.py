T = int(input())
for _ in range(T):
  VPS = input()
  cnt = 0
  for i in VPS:
    if i == '(':
      cnt +=1
    elif i ==')':
      cnt -=1
      if cnt < 0:
        break
  if cnt == 0:
    print('YES')
  else:
    print('NO')
