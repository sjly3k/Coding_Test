from _collections import deque

def dfs(x, y) :
    global home_num
    if x >= N or x <= -1 or y >= N or y <= -1 :
        return False
    if graph[x][y] == 1 :
        graph[x][y] = 0;
        home_num += 1;
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False;

def bfs(x, y) :
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0;
    cnt = 1;

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= N or ny >= N or nx < 0 or ny < 0:
                continue;
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0;
                cnt += 1
                queue.append((nx, ny))

    return cnt;


if __name__ == "__main__" :
    N = int(input())

    graph = []
    for _ in range(N) :
        tmp = list(map(int, input()))
        graph.append(tmp)

    res = 0
    apt = list()
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                apt.append(bfs(i, j))

    print(len(apt))
    apt.sort()
    for i in apt :
        print(i)

