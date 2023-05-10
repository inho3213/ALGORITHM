#백준 1406번 에디터
import sys

string = list(sys.stdin.readline().strip())
stack = []
M = int(sys.stdin.readline())
for _ in range(M):
  command = sys.stdin.readline().split()
  if command[0] == 'L' and string:
    stack.append(string.pop())
  elif command[0] == 'D' and stack:
    string.append(stack.pop())
  elif command[0] == 'B' and string:
    string.pop()
  elif command[0] == 'P':
    string.append(command[1])

string.extend(list(reversed(stack)))

print("".join(string))