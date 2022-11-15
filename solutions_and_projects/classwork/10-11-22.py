from random import randint


class Human:
    def __init__(self, name, criminal):
        self.name = name
        self.criminal = criminal

    def to_string(self):
        return f"{self.name} {self.criminal}"


names = ["Олег", "Егор", "Егор", "Егор", "Егор", "Егор", "Егор", "Егор", "Егор", "Егор", "Егор", "Егор",
         "Влад", "Семен", "Семен", "Семен", "Семен", "Семен", "Семен1", "Твоя мама"]

create_human = lambda: Human(names[randint(0, len(names) - 1)], False)


def set_crime(train):
    while True:
        van_n = randint(0, len(train) - 1)
        passenger_in_place = train[van_n][randint(0, len(train[van_n]) - 1)]
        if passenger_in_place:
            passenger_in_place.criminal = True
            break


train = []

for i in range(int(input("Введите к-во вагонов: "))):
    van = [create_human() if bool(randint(0, 1)) else None for _ in range(randint(2, 11))]
    train.append(van)

set_crime(train)

for i in range(len(train)):
    print(f"Вагон {i + 1}:")
    for passenger in train[i]:
        print(passenger.to_string() if passenger else "Пустое место")

criminal_found = False
for i in range(len(train)):
    print(f"Шериф вошел в вагон {i + 1}:")
    for j in range(len(train[i])):
        print(f"Шериф смотрит пассажира на месте {j}")
        passenger = train[i][j]
        if passenger:
            if passenger.criminal:
                print(f"Преступник найден в вагоне {i + 1} на месте {j}")
                criminal_found = True
                break
            else:
                print("Шериф идет к следующему месту")
        else:
            print("Место пустое")
    if criminal_found:
        break