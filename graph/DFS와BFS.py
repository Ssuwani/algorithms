# 1260 S2
from collections import deque
n, m, v = map(int, input().split())
graph = [[]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
[g.sort() for g in graph]
def dfs(visited, graph, start):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(visited, graph, i)

def bfs(visited, graph, start):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

visited = [False] * (n+1)
dfs(visited, graph, v)
print()
visited = [False] * (n+1)
bfs(visited, graph, v)