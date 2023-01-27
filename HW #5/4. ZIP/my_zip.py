# Завдання: написати свій власний zip


# 1. для объединения списков с одинаковым типом данных

# Списки из строк
goods = ['bread', 'milk', 'sausage']
description = ['wheaten', "cow's", 'premium']

result = [description[i] + ', ' + goods[i] for i in range(len(description))]
print(result) # ['wheaten, bread', "cow's, milk", 'premium, sausage']


# 2. для объединения списков с разными типами данных

# Список из строк + список из чисел
goods = ['bread', 'milk', 'sausage']
price = [1.20, 2.35, 5.60]

# список для записи результата
concat_list = []

# функция для конкатенации
def concat_lists(goods, price):
    new_price = list(map(str, price)) # привожу list of float к одному типу данных
    for i in range(len(goods)):
        concat_list.append(goods[i] + ', $' + new_price[i])
    return concat_list

concat_lists(goods, price)
print(concat_list) # ['bread, $1.2', 'milk, $2.35', 'sausage, $5.6']

# РЕЗЮМЕ:
# Вместе с тем, такой подход имет недостатоки:
# 1) необходимо приводить списки к одному типу данных
# 2) если один список будет больше, то произойдет ошибка. С zip такого не будет
# 3) увеличивается размер кода
# 4) если объеденять 3 или более списка - усложниться код. В таком случае, наверное,
# нужно будет объеденить 2-ва списка, потом в новый добавлять 3-й список.


# Вариант №2 с устранением проблемы разной длины списков

# С потерей части данных
goods = ['bread', 'milk', 'sausage']
price = [1.35, 2.55, 5.60, 3.14, 6.78, 8.99]

concat_list = []

def concat_lists(goods, price):
    # проверка длины списка
    if len (goods) > len (price):
        while len(goods) != len(price):
            goods.remove(goods[-1])
    if len (price) > len (goods):
        while len(price) != len(goods):
            price.remove(price[-1])
    # дальше код по аналогии с вариантом №2
    new_price = list(map(str, price))
    for i in range(len(goods)):
        concat_list.append(goods[i] + ', $' + new_price[i])
    return concat_list

concat_lists(goods, price)
print(concat_list) # ['bread, $1.35', 'milk, $2.55', 'sausage, $5.6']


# Без потери части данных
goods = ['bread', 'milk', 'sausage']
price = [1.35, 2.55, 5.60, 3.14, 6.78, 8.99]

concat_list = []

def concat_lists(goods, price):
    # проверка длины списка
    if len (goods) > len (price):
        while len(goods) != len(price):
            price.append('None')
    if len (price) > len (goods):
        while len(price) != len(goods):
            goods.append('None')
    # дальше код по аналогии с вариантом №2
    new_price = list(map(str, price))
    for i in range(len(goods)):
        concat_list.append(goods[i] + ', $' + new_price[i])
    return concat_list

concat_lists(goods, price)
print(concat_list)
# ['bread, $1.35', 'milk, $2.55', 'sausage, $5.6', 'None, $3.14', 'None, $6.78', 'None, $8.99']
