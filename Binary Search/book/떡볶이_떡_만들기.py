def binary_search_loop(array, target, start, end) :

    while start <= end :
        mid = (start + end) // 2
        tmp = 0;
        for i in range(N) :
            if array[i] - mid > 0 :
                tmp += array[i] - mid

        if tmp == target :
            return mid;
        elif tmp > target :
            start = mid + 1;
        else :
            end = mid - 1;

    return None;

# 머릿속에 있는 것 그대로 구현
# if __name__ == "__main__" :
#     N, M = map(int, input().split())
#     array = list(map(int, input().split()))
#     result_array = list()
#     for H in range(min(array) + 1, max(array) + 1):
#         result = 0;
#         for i in range(N):
#             if array[i] - H > 0:
#                 result += array[i] - H
#
#         if result == M:
#             result_array.append(H)
#
#     print(result_array)

# 이진 탐색 이용하여 구현
if __name__ == "__main__":
    N, M = map(int, input().split())
    array = list(map(int, input().split()))
    result_array = list()

    print(binary_search_loop(array, M, 0, max(array)))

