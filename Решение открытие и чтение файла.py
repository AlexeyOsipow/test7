Задача №1
from pprint import pprint
def make_cook_book(recipes_file):
    cook_book = {}
    with open(recipes_file, encoding='UTF-8') as file:
        for i in file:
            dish = i.strip()
            products = int(file.readline())
            cook_book_list = []
            for item in range(products):
                ingr = file.readline().split("|")
                ingredients = {'ingredient_name': ingr[0].strip(), 'quanity': int(ingr[1]), 'meacure': ingr[2].strip()}
                cook_book_list.append(ingredients)
            cook_book[dish] = cook_book_list
            file.readline()
    return cook_book

pprint(make_cook_book('recipes.TXT'), width=140)

# Задача №2


person_count = int(input('Введите количество человек: '))

def get_shop_list_by_dishes(dishes: list, file_name: str, person_count: int) -> dict:
    shop_list = {}
    cook_book = make_cook_book(file_name)
    for dish in dishes:
        for ingridient in cook_book.get(dish, []):
            if ingridient['ingredient_name'] in shop_list:
                shop_list[ingridient['ingredient_name']]['quanity'] += ingridient['quanity'] * person_count
            else:
                shop_list[ingridient['ingredient_name']] = {'quanity': ingridient['quanity'] * person_count, 'meacure': ingridient['meacure']}
    return shop_list


print(get_shop_list_by_dishes(["Фахитос", "Омлет"], 'recipes.TXT', person_count))



#Задание №3

import os
path = 'pythonProject3/'

def files(path: str):

    files_list = os.listdir(path)
    files_dict = {}

    for file_name in files_list:
        fil_txt = file_name.rfind('.txt', -4)
        if fil_txt >= 0:
            with open(os.path.join(path, file_name), 'r', encoding='utf-8') as file:
                files_dict[file_name] = file.readlines()

#
    with open("combination.txt", 'w', encoding='utf-8') as file:
        for file_name, rows in sorted(files_dict.items(), key=lambda x: len(x[1])):
            file.write(f"Название файла: {str(file_name)} \n")
            file.write(f"Кол-во строк - {str(len(rows))} \n\n")
            if '\n' not in rows[-1]:
                rows[-1] += '\n\n'
            file.write(''.join(rows))
print('Файл "comnination.txt" успешно загружен')
files(path)
