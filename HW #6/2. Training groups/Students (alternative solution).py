# Задача: Створити структуру даних для студентів з імен та прізвищ, можна
# випадкових. Придумати структуру даних, щоб вказувати, у якій групі навчається
# студент (Групи Python, FrontEnd, FullStack, Java).
# Студент може навчатися у кількох групах. Потім вивести:
# 1) студентів, які навчаються у двох та більше групах
# 2) студентів, які не навчаються на фронтенді
# 3) студентів, які вивчають Python або Java


students = {
    "Ivanov": {'name': 'Ivan', 'course': 'FrontEnd'},
    "Petrov": {'name': 'Petr', 'course': 'Python'},
    "Sidorov": {'name': 'Sidor', 'course': ['Java', 'Python']},
    "Bananov": {'name': 'Banan', 'course': 'FullStack'},
    "Apelsinov": {'name': 'Apelsin', 'course': ['Java', 'FullStack']},
    "Mandarinov": {'name': 'Mandarin', 'course': 'Python'},
    "Marmeladov": {'name': 'Marmelad', 'course': 'Java'},
    "Vinogradov": {'name': 'Kish_Mish', 'course': ['Python', 'FrontEnd']},
    "Shokoladova": {'name': 'Korona', 'course': 'Java'},
    "Yablokov": {'name': 'Red_Chif', 'course': ['Python', 'FullStack']},
}
# 1. студенти, які навчаються у двох та більше групах
for username, userinfo in students.items():
    course = userinfo['course']
    if type(course) == list:
        print(f'Студент: {username} учится в 2 и более группах')

print('\n' + '***'*20)

# 2. студенти, які не навчаються на фронтенді
for username, userinfo in students.items():
    course = userinfo['course']
    if course == 'Python' or course == 'Java':
           print(f'Студент: {username} не учится на FrontEnd')

print('\n' + '***'*20)

# 3. студенти, які вивчають Python або Java
for username, userinfo in students.items():
    course = userinfo['course']
    if course == 'Python' or course == 'Java':
           print(f'Студент: {username} учится на Python или Java')

print('\n' + '***'*20)

# 4. студенти, які навчаються на фронтенді
for username, userinfo in students.items():
    course = userinfo['course']
    if course == 'FrontEnd' or course == 'FullStack':
           print(f'Студент: {username} учится на FrontEnd')
    if type(course) == list:
        for index in course:
            if index == 'FrontEnd' or index == 'FullStack':
                print(f'Студент: {username} учится на FrontEnd')
