from statistics import mean
from random import randint

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
    for i in range(1, len(arr)-1, 2):
        arr[i] = arr[i] * 2
    return arr

# print(task3(array_for_test))

def task4(arr):
    third = len(arr) // 3
    for i in range(len(arr) - 1):
        if third <= i < 2*third:
            arr[i] = 1
    return arr

# print(task4(array_for_test))

def task5(arr):
    n = arr[-1]
    for i in range(0, len(arr)-1, 4):
        arr[i] = n
    return arr

# print(task5(array_for_test))

def task6(arr):
    for i in range(len(arr)-1):
        if arr[i] > 10: arr[i] *= -1
    return arr

# print(task6(array_for_test))

def task7(arr, ellements):
    for i in range(ellements):
        arr.insert(0, 0)
    return arr

# print(task7(array_for_test, 3))

# def task8(arr):


# print(task8(array_for_test))

def task9(arr):
    list_n = []
    for i in range(0, len(arr), 2):
        if arr[i] > 0:
            list_n.append(arr[i])
    return list_n

# print(task9(array_for_test))

def task10(len):
    return [i**2 + 10 for i in range(len-1)]

# print(task10(100))

def task11(arr):
    return mean(arr)

# print(task11(array_for_test))

def task12(arr):
    lst = []
    for i in arr:
        if i > 0: lst.append(i)
    avg = sum(lst) / len(lst)
    var = sum((x - avg) ** 2 for x in lst) / len(lst)
    return var

# print(task12(array_for_test))

def task13(arr):
    for i in arr:
        if i > 0 and i % 2 == 0:
            return True
        else:
            return False

# print(task13(array_for_test))

def task14(arr):
    counter_list = []
    counter = 1
    for i in range(len(arr)-1):
        if arr[i]+1 == arr[i+1]:
            counter += 1
        else:
            counter_list.append(counter)
            counter = 1
    counter_list.append(counter)
    return max(counter_list)

array14 = [2,4,5,1,2,3,4,5]

# print(task14(array14))

#?????????????? ?????? ?????????????????????? ?? ????????????????

class Soldier:
    def __init__(self):
        self.min = 1
        self.max = 10
    def to_go(self):
        way = randint(self.min, self.max)
        return way

class Flyer(Soldier):
    def __init__(self):
        self.min = 20
        self.max = 50

class Submariner(Soldier):
    def __init__(self):
        self.min = 5
        self.max = 15

def set_army():
    army = []
    for i in range(25):
        # if randint(0, 1):
        #     army.append(Submariner())
        # else:
        #     army.append(Flyer())
        army.append(Flyer() if randint(0,1) else Submariner())
    return army

def count_distance(army):
    total_way = 0
    for soldier in army:
        total_way += soldier.to_go()
    return total_way

def count_av_distance(army):
    submariners_total, counter = 0, 0
    for soldier in army:
        if isinstance(soldier, Submariner):
            counter += 1
            submariners_total += soldier.to_go()
    return submariners_total / counter

# print(count_distance(set_army()), "km")
# print(count_av_distance(set_army()), "km")

#???????????? ?????? ??????????????
class Cup():
    def __init__(self):
        self.amount = randint(0, 9999)

bank = [Cup() for i in range(randint(1, 50))]
