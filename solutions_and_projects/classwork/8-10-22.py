def compare(a, b):
    if a > b:
        return "a больше b"
    elif b > a:
        return "b больше a"
    else:
        return "a равно b"


a = int(input("Введите а: "))
b = int(input("Введите b: "))
while True:
    q = input("Введите действие (?, +, -, *, /): ")
    if q == "?":
        print(compare(a, b))
    elif q == "+":
        print(f"Cумма = {a + b}")
    elif q == "-":
        print(f"Разность = {a - b}")
    elif q == "*":
        print(f"Произведение = {a * b}")
    elif q == "/":
        print(f"Частное = {a / b}")
    else:
        print("Вы ввели некорректное действие")
        continue
    break
