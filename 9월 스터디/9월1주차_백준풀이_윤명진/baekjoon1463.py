from collections import deque
N = int(input())

# bfs로 구현
def bfs(n):
    # n이 1인 경우 0 출력
    if n == 1:
        return 0
    
    # n이 1이 아닌 경우
    q = deque([[n, 0]])
    
    # n 방문 처리
    visited = [0] * (10 ** 6 + 1)
    visited[n] = 1
    
    # n과 연산 횟수를 q에서 꺼내서 탐색
    while q:
        now, count = q.popleft()
        
        # 다음 위치가 n/3, n/2, n=2인 경우 다음 연산에서 1이 되므로 count에 1 더한 값을 반환
        if now / 3 == 1 or now / 2 == 1 or now - 1 == 1:
            return count + 1

        # 3으로 나누어 떨어지고 범위 내에 있으며, 방문하지 않은 경우
        if now % 3 == 0 and 1 <= now // 3 <= 10 ** 6 and visited[now//3] == 0:
            # q에 3으로 나눈 몫과 count+1을 q에 추가한 다음, 방문처리
            q.append([now // 3, count + 1])
            visited[now // 3] = 1
        
        # 마찬가지로 2로 나누어 떨어지거나 1을 빼는 경우도 위와 같은 방법으로 방문
        if now % 2 == 0 and 1 <= now // 2 <= 10 ** 6 and visited[now//2] == 0:
            q.append([now // 2, count + 1])
            visited[now // 2] = 1

        if 1 <= now - 1 <= 10 ** 6 and visited[now - 1] == 0:
            q.append([now - 1, count + 1])
            visited[now - 1] = 1

result = bfs(N)
print(result)