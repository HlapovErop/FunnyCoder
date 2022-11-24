array_for_test = [1, 10, 40, 43, 23, 22, 72, 12, 74, 3, 6, 23, 732, 101, -3]

def task1(arr):
    arr[0], arr[-1] = arr[-1], arr[0]
    return arr

# print(task1(array_for_test))

def task2(arr):
    for i in range(0, len(arr)-1, 2):
        arr[i] = 0
    return arr

# print(task2(array_for_test))

def task3(arr):
    for i in range(0, len(arr)-1, 2):
        arr[i] = arr[i] * 2
    return arr

# print(task3(array_for_test))

def task4(arr):
    third = len(arr) / 3
    for i in range(len(arr) - 1):
        if third <= i < 2*third:
            arr[i] = 1
    return arr

# print(task4(array_for_test))

def task5(arr):
