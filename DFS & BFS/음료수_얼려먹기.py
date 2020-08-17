def dfs(x, y) :
    if x <= -1 or x >= N or y <= -1 or y >= M : return False
    if graph[x][y] == 0 :
        graph[x][y] = 1;
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x, y-1)
        return True
    return False;

if __name__ == "__main__" :
    N, M = map(int, input().split())
    graph = list()

    for _ in range(N) :
        line = list(map(int, input()))
        graph.append(line)

    result = 0;
    for i in range(N) :
        for j in range(M) :
            if dfs(i, j) == True :
                result += 1;



