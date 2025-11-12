from collections import deque

n = int(input())

person_1, person_2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [-1 for _ in range(n + 1)]
visited[person_1] = 0
queue = deque()
queue.append(person_1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

while queue:
    current = queue.popleft()

    if current == person_2:
        break

    for next_person in graph[current]:
        if visited[next_person] == -1:
            visited[next_person] = visited[current] + 1
            queue.append(next_person)

result = visited[person_2]
print(result)