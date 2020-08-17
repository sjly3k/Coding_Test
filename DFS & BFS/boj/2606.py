from _collections import deque

def dfs(graph, v, visited) :
    global result;
    visited[v] = True
    result.append(v)
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)

def bfs(graph, start, visited) :
    global result;
    visited[start] = True
    queue = deque()
    queue.append((start))

    while queue:
        v = queue.popleft()
        result.append(v)
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True


if __name__ == "__main__" :
    N = int(input())
    M = int(input())

    graph_all = []
    for _ in range(M) :
        graph_all.append(list(map(int, input().split())))

    graph = [ [] for i in range(N + 1) ]
    for num_list in graph_all :
        graph[num_list[0]].append(num_list[1])
        graph[num_list[1]].append(num_list[0])

    for i in range(N + 1) :
        graph[i].sort()

    visited = [False] * (N + 1)
    result = list()
    # dfs(graph, 1, visited)
    bfs(graph, 1, visited)
    print(len(result) - 1)
