n = int(input())
stack = []
ans = []
cnt = 1
temp = True
for _ in range(n):
  num = int(input())
  while cnt <= num:
    stack.append(cnt)
    ans.append('+')
    cnt += 1

  if stack[-1] == num:
    stack.pop()
    ans.append('-')
  else:
    temp = False
    print("NO")
    break
if temp == True:
  for i in ans:
    print(i)