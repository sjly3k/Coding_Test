def dfs(x, y) :
    if x >= N or y >= M or x < 0 or y < 0 :
        return False;
    if graph[x][y] == 1:
        graph[x][y] = 0;
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True;
    return False;

if __name__ == "__main__" :
    T = int(input())


    for _ in range(T):
        M, N, K = map(int, input().split())
        graph = [[0] * M for _ in range(N)]
        for _ in range(K):
            x, y = map(int, input().split())
            graph[y][x] = 1

        res = 0
        for i in range(N):
            for j in range(M):
                if dfs(i, j) == True:
                    res += 1

        print(res)