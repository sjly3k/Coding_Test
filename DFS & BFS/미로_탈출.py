from _collections import deque

def bfs(x, y) :
    queue = deque()
    queue.append((x, y))

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue :
        x, y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M :
                continue;
            if maze[nx][ny] == 0 :
                continue;
            if maze[nx][ny] == 1:
                queue.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1

    return maze[N-1][M-1]


if __name__ == "__main__" :
    N, M = map(int, input().split())
    maze = list()
    for _ in range(N):
        maze.append(list(map(int, input())))

    print(maze)
    print(bfs(0, 0))
    print(maze)