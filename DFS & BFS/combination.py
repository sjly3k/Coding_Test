# 조합의 경우, 중요한 것은 traverse 할때, 다음 시작점을 가지고 간다는 것!

def dfs(L, beginWith) :
    if L == r:
        print(result)
        return None;
    else :
        for i in range(beginWith, len(n)):
            if not visited[i]:
                visited[i] = True
                result[L] = n[i]
                dfs(L+1, i+1)
                visited[i] = False


if __name__ == "__main__" :
    n = [1, 2, 3]
    r = 2
    result = [0] * r
    visited = [False] * len(n)

    dfs(0, 0)