N, K = map(int, input().split())
chk = []
people = [i for i in range(1, N+1)]
num = 0
for _ in range(N):
  num += K-1 #인덱스
  if num >= len(people):
    num = num%len(people)
  chk.append(str(people.pop(num)))
print("<", ', '.join(chk), ">", sep="")