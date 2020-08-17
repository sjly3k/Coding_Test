from _collections import deque

def dfs(graph, v, visited) :
    visited[v] = True
    print(v, end = " ")
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)

def bfs(graph, start, visited) :
    visited[start] = True
    queue = deque([start])

    while queue :
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True;



if __name__ == "__main__" :
    N, M, V = map(int, input().split())
    graph_all = []
    for _ in range(M) :
        graph_all.append(list(map(int, input().split())))

    graph = [ [] for i in range(N + 1) ]
    for num_list in graph_all :
        graph[num_list[0]].append(num_list[1])
        graph[num_list[1]].append(num_list[0])

    for i in range(N + 1) :
        graph[i].sort()


    visited = [False] * (N + 1);
    dfs(graph, V, visited)
    print()
    visited = [False] * (N + 1);
    bfs(graph, V, visited)
