passenger_baggage = {
    1: (3, 50),
    2: (1, 20),
    3: (2, 45),
    4: (4, 55),
    5: (5, 30),
    6: (1, 15),
    7: (2, 40),
    8: (3, 60),
    9: (1, 24),
    10: (2, 25)
}

def add_baggage():
    passenger_id = int(input("Введіть номер пасажира: "))
    if passenger_id in passenger_baggage:
        print("Цей пасажир вже існує в системі.")
        return
    items = int(input("Введіть кількість речей: "))
    weight = float(input("Введіть загальну вагу (в кг): "))
    passenger_baggage[passenger_id] = (items, weight)
    print("Дані додано успішно.")

def remove_baggage():
    passenger_id = int(input("Введіть номер пасажира для видалення: "))
    if passenger_id in passenger_baggage:
        del passenger_baggage[passenger_id]
        print("Дані видалено успішно.")
    else:
        print("Пасажир з таким номером не знайдений.")


def analyze_more_than_two_items():
    more_than_two_items_count = sum(1 for items, weight in passenger_baggage.values() if items > 2)
    print("Кількість пасажирів, які мають більше двох речей:", more_than_two_items_count)


def analyze_one_item_under_25kg():
    one_item_under_25kg = any(items == 1 and weight < 25 for items, weight in passenger_baggage.values())
    print("Чи є пасажир з однією річчю вагою менше 25 кг:", "Так" if one_item_under_25kg else "Ні")


def analyze_weight_difference():
    if passenger_baggage:
        average_weight_per_item = sum(weight / items for items, weight in passenger_baggage.values()) / len(
            passenger_baggage)

        matching_baggage_numbers = [
            passenger_id for passenger_id, (items, weight) in passenger_baggage.items()
            if abs((weight / items) - average_weight_per_item) <= 0.5
        ]
    else:
        matching_baggage_numbers = []

    print("Номери багажів, що відповідають умові:", matching_baggage_numbers if matching_baggage_numbers else "Немає")


def print_sorted_baggage():
    sorted_baggage = {k: passenger_baggage[k] for k in sorted(passenger_baggage)}
    print("Відсортований список пасажирів за номерами:")
    for passenger_id, (items, weight) in sorted_baggage.items():
        print(f"Пасажир {passenger_id}: кількість речей = {items}, загальна вага = {weight} кг")


while True:
    print("\nМеню:")
    print("1. Додати дані про багаж пасажира")
    print("2. Видалити дані про багаж пасажира")
    print("3. Аналіз багажу:")
    print("    3a. Кількість пасажирів з більше ніж двома речами")
    print("    3b. Чи є пасажир з однією річчю вагою менше 25 кг")
    print("    3c. Номер багажу, де вага однієї речі відрізняється від середньої не більше ніж на 0,5 кг")
    print("4. Вивести відсортований список пасажирів за номерами")
    print("5. Вийти")
    choice = input("Виберіть опцію: ")

    if choice == '1':
        add_baggage()
    elif choice == '2':
        remove_baggage()
    elif choice == '3a':
        analyze_more_than_two_items()
    elif choice == '3b':
        analyze_one_item_under_25kg()
    elif choice == '3c':
        analyze_weight_difference()
    elif choice == '4':
        print_sorted_baggage()
    elif choice == '5':
        print("Вихід з програми.")
        break
    else:
        print("Невірний вибір, спробуйте ще раз.")

