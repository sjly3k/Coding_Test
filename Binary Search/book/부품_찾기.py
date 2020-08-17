def binary_search(array, target, start, end) :
    if start > end :
        return None;

    mid = (start + end) // 2

    if array[mid] == target :
        return mid;
    elif array[mid] > target :
        return binary_search(array, target, start, mid - 1)
    else :
        return binary_search(array, target, mid + 1, end)


if __name__ == "__main__" :
    N = int(input())
    array_N = list(map(int, input().split()))

    # Binary Search는 무조건 모든 원소가 정렬이 되어있는 상태여야 함.
    array_N.sort()

    M = int(input())
    array_M = list(map(int, input().split()))

    for item in array_M:
        result = binary_search(array_N, item, 0, len(array_N) - 1)
        if result is not None:
            print('yes', end=" ")
        else:
            print('no', end=" ")
