array_for_test = [1, 45, 56, 545, 65, 6]


def task2(array):
    return [0 if i % 2 == 0 else el for i, el in enumerate(array)]


print(task2(array_for_test))
