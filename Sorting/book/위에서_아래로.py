if __name__ == "__main__" :
    N = int(input())
    array = list()
    for _ in range(N) :
        array.append(int(input()))

    array = sorted(array, reverse=True)
    for num in array:
        print(num, end=" ")