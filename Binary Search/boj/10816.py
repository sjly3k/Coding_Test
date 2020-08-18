from sys import stdin

def binary_search(array, target, start, end) :
    if start > end :
        return 0

    mid = (start + end) // 2
    if array[mid] == target :
        return array[start : end + 1].count(target);
    elif array[mid] > target :
        return binary_search(array, target, start, mid - 1)
    else :
        return binary_search(array, target, mid + 1, end)

if __name__ == "__main__" :
    N = int(input())
    array_sanggeun = sorted(list(map(int, stdin.readline().split())))
    M = int(input())
    array_target = list(map(int, stdin.readline().split()))

    n_dict = {}
    for i in range(M):
        if i not in n_dict:
            n_dict[array_target[i]] = binary_search(array_sanggeun, array_target[i], 0, N - 1)

    print(list(n_dict.values()))