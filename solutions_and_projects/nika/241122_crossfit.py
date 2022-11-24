from statistics import mean

array_for_test = [1, 45, 545, 65, 6]
array2_for_test = [1, 45, 545, 65, 6]
array3_for_test = [1, 45, 545, 65, 6]
array4_for_test = [1, 45, 545, 65, 6]
array5_for_test = [1, 45, 545, 65, 6]
array6_for_test = [1, 45, 545, 65, 6]
array7_for_test = [1, 45, 545, 65, 6]
array8_for_test = [-1, 45, -545, 65, 6]
array10_for_test = [-1, 45, -545, 65, 6]
array131_for_test = [-1, -45, -545, 65, -6]
array132_for_test = [1, 45, -545, -65, 6]


def task1(array):
    array[0], array[-1] = array[-1], array[0]
    return array


def task2(array):
    for i in range(len(array)):
        if i % 2 == 0:
            array[i] = 0
    return array


def task3(array):
    for i in range(len(array)):
        if i % 2 == 1:
            array[i] *= 2
    return array


def task4(array):
    l1_3 = len(array) // 3
    for i in range(len(array)):
        if i >= l1_3 and i <= l1_3 * 2:
            array[i] = 1
    return array


def task5(array):
    n = array[-1]
    for i in range(2, len(array), 4):
        array[i] = n
    return array


def task6(array):
    for i in range(len(array)):
        if array[i] > 10:
            array[i] *= -1
    return array


def task7(array, numb):
    for i in range(numb):
        array.insert(0, 0)
        array.pop(-1)
    return array


def task8(array):
    result = []
    for el in array:
        if el > 0:
            result.append(el)
    return result


def task9(numb):
    return [i ** 2 + 10 for i in range(numb)]


def task10(array):
    for i in range(1, len(array), 2):
        array[i], array[i - 1] = array[i - 1], array[i]
    return array


def task11(array):
    return mean(array)


def task13(array):
    for el in array:
        if el > 0 and el % 2 == 0:
            return True
    return False


def task14(array):
    max_value = 0
    count = 0
    for i in range(len(array) - 1):
        if array[i]

print(task1(array_for_test))
print(task2(array2_for_test))
print(task3(array3_for_test))
print(task4(array4_for_test))
print(task5(array5_for_test))
print(task6(array6_for_test))
print(task7(array7_for_test, 2))
print(task8(array8_for_test))
print(task9(6))
print(task10(array10_for_test))
print(task13(array131_for_test))
print(task13(array132_for_test))

