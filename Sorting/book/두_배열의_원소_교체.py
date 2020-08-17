if __name__ == "__main__" :
    N, K = map(int, input().split())
    array = list()
    for _ in range(2) :
        tmp = list(map(int, input().split()))
        tmp = sorted(tmp)
        array.append(tmp)

    print(array)
    array[1] = sorted(array[1], reverse=True)

    for i in range(K):
        if array[0][i] < array[1][i] :
            array[0][i] = array[1][i]

    print(array)
    print(sum(array[0]))