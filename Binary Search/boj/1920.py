def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2

    if array[mid] == target:
        return 1
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)

if __name__ == "__main__" :
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    M = int(input())
    B = list(map(int, input().split()))

    for i in B:
        print(binary_search(A, i, 0, N - 1))