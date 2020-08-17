def dfs(L) :
    if L == r :
        print(result)
        return None;
    else :
        for i in range(len(n)) :
            if checkList[i] is not True:
                checkList[i] = True
                result[L] = n[i]
                dfs(L+1)
                checkList[i] = False


if __name__ == "__main__" :
    n = [1, 2, 3]
    r = 2;
    result = [0] * r;
    checkList = [False] * len(n)

    dfs(0)