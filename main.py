import os.path
import os

with open('recipies.txt', encoding='utf-8') as file:
    cook_book = {}
    for i in file:
        recepie_name = i.strip()
        ingredients_count = file.readline()
        ingredients = []
        for p in range(int(ingredients_count)):
            recepie = file.readline().strip().split(' | ')
            ingredient, quantity, measure = recepie
            ingredients.append({'ingredient': ingredient, 'quantity': quantity, 'measure': measure})
        file.readline()
        cook_book[recepie_name] = ingredients
    print(cook_book)


def get_shop_list_by_dishes(person_count: int, dishes: list):
    order = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['ingredient'] in order:
                    order[consist['ingredient']]['quantity'] += consist['quantity'] * person_count
                else:
                    order[consist['ingredient']] = {'measure': consist['measure'],
                                                     'quantity': (consist['quantity'] * person_count)}
        else:
            print('Такого блюда нет в книге')
    print(order)


get_shop_list_by_dishes(2, ['Запеченный картофель', 'Омлет'])







