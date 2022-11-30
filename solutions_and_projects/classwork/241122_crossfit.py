from statistics import mean
from random import randint

array_for_test = [1, 45, 56, 545, 65, 6]
array2_for_test = [1, 45, 56, 545, 65, 6]
array3_for_test = [1, 45, 56, 545, 65, 6]
array4_for_test = [1, 45, 56, 545, 65, 6]
array5_for_test = [1, 45, 56, 545, 65, 6, 8, 4, 6, 8, 2, 5, 9, 10]
array6_for_test = [1, 45, 56, 545, 65, 6]
array7_for_test = [1, 45, 56, 545, 65, 6]
array8_for_test = [1, 45, 56, -545, 65, 6, -4, -94]
array9_for_test = [1, 45, 56, -545, 65, 6, -4, -94]
array10_for_test = [1, 45, 56, -545, 65, 6, -4, -94]
array11_for_test = [1, 45, 56, -545, 65, 6, -4, -94]
array111_for_test = [1, 45, 56, -545, 65, 6, -4, -94]
array131_for_test = [-1, -45, -56, -545, -65, -6]
array132_for_test = [1, -45, -56, 545, 65, 6]
array14_for_test = [0, 1, 3, 6, 7, 8, 7]
array18_for_test = [0, 1, 3, 6, 7, 8, 7]
array19_for_test = [0, 1, 3, 5, 6, 7, 8, 5, 5555]


def task1(array):
    array[0], array[-1] = array[-1], array[0]
    return array


def task11(array):
    temp = array[0]
    array[0] = array[-1]
    array[-1] = temp
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
        elif i % 2 == 0:
            array[i] /= 2
    return array


def task4(array):
    l1_3 = len(array) // 3
    for i in range(len(array)):
        if l1_3 <= i < l1_3 * 2:
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


def task91(numb):
    result = []
    for i in range(numb):
        result.append(i ** 2 + 10)
    return result


def task10(array):
    for i in range(1, len(array), 2):
        array[i], array[i - 1] = array[i - 1], array[i]
    return array


def task11(array):
    return mean(array)


def task111(array):
    sum = 0
    cnt = 0
    for el in array:
        sum += el
        cnt += 1
    return sum / cnt
    # return sum(array) / len(array)


def task13(array):
    for el in array:
        if el > 0 and el % 2 == 0:
            return True
    return False


def task14(array):
    max_value = 0
    count = 0
    for i in range(len(array) - 1):
        if array[i] + 1 == array[i + 1]:
            count += 1
        else:
            max_value = max(count, max_value)
    return max(count, max_value)


def task15(k):
    i = 0
    while i >= i * i / k:
        i += 1
    return i


class Task16:
    def __init__(self, idk, idk2, idk3):
        self.idk = idk
        self.idk2 = idk2
        self.__idk3 = idk3

    def get_idk3(self):
        return self.__idk3

    def set_idk3(self, value):
        self.__idk3 = value


ex1 = Task16(1, 2, 3)
ex2 = Task16(228, 100500, 123)


# print(ex1.get_idk3())
# # ex1.set_idk3(int(input()))
# print(ex1.get_idk3())
# print(ex1.__idk3)

def task18(array):
    max_value = array[0]
    for el in array:
        if el > max_value:
            max_value = el
    return max_value


def task19(array):
    min_value = array[0]
    for el in array:
        if el < min_value:
            min_value = el
    value = min_value + 5
    i = 0
    for el in array:
        if el == value:
            i += 1
    return i


# def task20():
#     return [randint(20, 200) for i in range(0, 10)]
task20 = lambda: [randint(20, 200) for i in range(0, 10)]

task21 = lambda n: [task20() for i in range(n)]

def task22():
    class RandomNumber():
        def __init__(self):
            self.value = randint(0, 200)
    array = [RandomNumber() for i in range(10)]
    for el in array:
        if el.value > 100:
            print(f"элемент-{el.value}, ", end="")
    print()

print(task1(array_for_test))
print(task2(array2_for_test))
print(task3(array3_for_test))
print(task4(array4_for_test))
print(task5(array5_for_test))
print(task6(array6_for_test))
print(task7(array7_for_test, 2))
print(task8(array8_for_test))
print(task9(5))
print(task10(array10_for_test))
print(task11(array11_for_test))
print(task111(array111_for_test))
print(task13(array131_for_test))
print(task13(array132_for_test))
print(task14(array14_for_test))
print(task15(2))
print(task18(array18_for_test))
print(task19(array19_for_test))
print(task20())
print(task21(2))
task22()

