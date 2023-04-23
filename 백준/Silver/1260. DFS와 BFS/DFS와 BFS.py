N, M, V = map(int,input().split())
# N : 정점 / M : 간선 / V : 시작노드

from collections import deque
#인접 행렬 만들기
#True, False로 구현
graph = [[False]*(N+1) for i in range(N+1)]

for i in range(M):
  a, b = map(int, input().split())
  graph[a][b] = True
  graph[b][a] = True
#서로 연결된 노드들은 True로 안된 노드들은 False로 구현함

#방문 처리한거
ans_dfs = [False] * (N+1)
ans_bfs = [False] * (N+1)

def dfs(V):
  ans_dfs[V] = True #해당 노드값 방문처리
  print(V, end = ' ')
  for i in range(1, N+1):
    if not ans_dfs[i] and graph[V][i]:   #만약 i를 아직 방문하지 않았고, V노드와 연결이 되어있다면~ 실행
      dfs(i)


def bfs(V):
    q = deque([V]) 
    ans_bfs[V] = True  # 해당 V 값을 방문처리
    while q:  # q가 빌때까지 돈다.
        V = q.popleft()  # 큐에 있는 첫번째 값 꺼낸다.
        print(V, end=" ")  # 해당 값 출력
        for i in range(1, N + 1):
            if not ans_bfs[i] and graph[V][i]:  # 만약 해당 i값을 방문하지 않았고 V와 연결이 되어 있다면
                q.append(i)  # 그 i 값을 추가
                ans_bfs[i] = True  # i 값을 방문처리


dfs(V)
print()
bfs(V)
