from utils import logging_time
import random
import copy

@logging_time
def selection_sort(array):
    # 맨 처음 위치한 원소는 고정, 나머지 원소중 가장 작은 원소를 찾아 맨 처음 원소와 교체
    # 위 작업을 반복하여 정렬 진행
    # e.g) step 1 : index=0 고정, 1~N 까지 중 가장 작은 원소와 0번 원소 변경
    #      step 2 : index=1 고정, 2~N 까지 중 가장 작은 원소와 1번 원소 변경
    #      step N : index=N 고정, 더 이상 원소가 남아있지 않으므로 정렬된 array 반환하고 종료
    # Time Complexity : O(N^2)

    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

@logging_time
def insertion_sort(array) :
    # 본 정렬은 2번째 index부터 시작하는데, 앞의 숫자들은 모두 정렬되어 있다고 가정하고 시작한다.
    # e.g) step 1 : index=1, 0~1번 까지 중에, 왼쪽에 있는 원소와 차례차례 비교를 실행하고, 1번이 0번보다 작다면, 0번과 1번을 교환한다.
    #      step 2 : index=2, 0~2번 까지 중에, 위의 step 1을 반복한다.

    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break

    return array

@logging_time
def quick_sort(array, start, end):
    if start >= end :
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot] :
            left += 1;
        while right > start and array[right] >= array[pivot] :
            right -= 1;
        if left > right :
            array[right], array[pivot] = array[pivot], array[right]
        else :
            array[left], array[pivot] = array[pivot], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

def quick_sort_pythonic(array) :
    if len(array) <= 1 :
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort_pythonic(left_side) + [pivot] + quick_sort_pythonic(right_side)

@logging_time
def counting_sort(array) :
    counting = [0] * (max(array) + 1)
    for num in array:
        counting[num] += 1;

    result = list()
    for i in range(len(counting)):
        for j in range(counting[i]) :
            result.append(i)
    return result



if __name__ == "__main__":
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    new_array = list()
    for i in range(100):
        new_array.append(random.randint(0, 100))



    print("Selection Sort N = 10 :", selection_sort(copy.deepcopy(array)))
    print("Insertion Sort N = 10 :", insertion_sort(copy.deepcopy(array)))
    print("Counting Sort N = 10 :", counting_sort(copy.deepcopy(array)))

    print("Selection Sort N = 100 :", selection_sort(copy.deepcopy(new_array)))
    print("Insertion Sort N = 100 :", insertion_sort(copy.deepcopy(new_array)))
    print("Counting Sort N = 100 :", counting_sort(copy.deepcopy(new_array)))
    # quick_sort_pythonic(new_array)
    # quick_sort(new_array, 0, len(new_array) - 1)
    # print("N = 100 :", new_array)
