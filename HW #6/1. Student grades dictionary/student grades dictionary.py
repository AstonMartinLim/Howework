# Створити словник оцінок передбачуваних студентів
# (Ключ – ПІ студента, значення – список оцінок студентів).
# Знайти найуспішнішого і самого слабенького за середнім балом.

students = {
    "Yablokov": [2, 4, 5, 5, 3],
    "Vinogradov": [3, 3, 4, 4],
    "Shokoladov": [5, 5, 4, 5, 4],
    "Bananov": [2, 2, 3, 2, 3, 3],
    "Apelsinov": [4, 4, 3, 5, 5],
    "Mandarinov": [4, 4, 5, 5],
    "Marmeladov": [3, 4, 5]
}

def calc_average (lst):
    return sum(lst) / len(lst)


def find_best (students):
    name = ' '
    best = 0
    for key, val in students.items():
        avg = round(calc_average (val), 2)
        if avg > best:
            best = avg
            name = key
    return (name, best)
        

def find_loser (students):
    name = ' '
    loser = 6
    for key, val in students.items():
        avg = round(calc_average (val), 2)
        if avg < loser:
            loser = avg
            name = key
    return (name, loser)

print(find_best (students)) # ('Shokoladov', 4.6)
print(find_loser (students)) # ('Bananov', 2.5)
