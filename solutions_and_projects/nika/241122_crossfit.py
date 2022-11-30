from random import randint
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
array19_for_test = [0, 8, 5, 34, 6, 5]


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


class Task16:
    def __init__(self, idk, idk2, idk3):
        self.idk = idk
        self.idk2 = idk2
        self.__idk3 = idk3

    def get_idk3(self):
        return self.__idk3

    def set_idk3(self, value):
        self.__idk3 = value

ex1 = Task16(1,2,3)
# print(ex1.get_idk3())
# ex1.set_idk3(input())
# print(ex1.get_idk3())

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

task20 = lambda: [randint(20, 200) for i in range(0, 10)]

task21 = lambda n: [task20() for i in range(n)]

def task22():
    class RandomNumber():
        def init(self):
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
print(task9(6))
print(task10(array10_for_test))
print(task13(array131_for_test))
print(task13(array132_for_test))
print(task19(array19_for_test))
print(task21(5))
task22()
