if __name__ == "__main__" :
    N = int(input())
    array = list()
    for _ in range(N) :
        name, score = input().split()
        array.append((name, score))

    print(array)
    array = sorted(array, key=lambda student: student[1])
    for student in array:
        print(student[0], end=" ")