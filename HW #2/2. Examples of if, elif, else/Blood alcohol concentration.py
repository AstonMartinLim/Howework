print("""This the program determines the blood alcohol content and shows the effects \
of different levels of alcohol in the blood""")

b1 = """Поведение: В среднем поведение нормальное \n
Нарушения: Скрытые проявления, которые могут быть обнаружены специальными тестами"""

b2 = """Поведение: Средневыраженная эйфория, Расслабление, Ощущение радости, Говорливость, Понижение сдержанности \n
Нарушения: Концентрация"""

b3 = """Поведение: Притупление ощущения, Расторможенность, Экстравертность \n
Нарушения: Рассуждение, Глубина восприятия, Периферическое зрение, Приспособление зрачка к свету"""

b4 = """Поведение: Сверх-экспрессивность, Переменчивость эмоций, Гнев или печаль, Неистовость, Снижение либидо \n
Нарушения: Рефлексы, Время реакции, Основные моторные навыки, Способность к контролю движения (появляется шатающаяся походка),
Нечленораздельная речь, Эрекция (у мужчин, временно), Вероятность временного алкогольного отравления"""

b5 = """Поведение: Ступор, Потеря способности к пониманию, Ослабление способностей к ощущению, Вероятность потери сознания \n
Нарушения: Тяжелое нарушение моторики, Потеря сознания, Потеря памяти"""

b6 = """Поведение: Сильное угнетение функций центральной нервной системы, Потеря сознания, Вероятность смерти
Нарушения: Контроль над мочеиспусканием, Дыхание, Чувство равновесия (полная утрата), Сердцебиение"""

b7 = """Поведение: Полная утрата контроля за поведением, Потеря сознания, Вероятность смерти
Нарушения: Дыхание, Сердцебиение, Контроль над движением зрачков (Нистагм)"""

b8 = """Поведение: Высокий риск отравления, Высокий риск смерти"""

sex = input("Do you men (type 'm') or women (type 'w'): ")
weight = float(input("Please, type your weight (in kg): "))
print('\n')

if sex == 'm':
    print("""What type of alcohol did you drink?
Note: You can choose only one type of alcohol""")

    type_alc = input("Vodka (type 'v'), Beer (type 'b'). Yours choose is: ")
    print('\n')
      
    if type_alc == 'v':
        kol_vo = int(input("""How much vodka did you drink?
Note: 1 = 100 ml of alcohol with a strength of 40% vol, etc. Your choice: """))
        massa = kol_vo * 40.0
        promil = round ((massa / (weight * 0.7)), 2)

        if (promil >= 0) and (promil < 0.20):
            print("Blood alcohol concentration:", promil, "Not yet evening!")
        elif (promil >= 0.20) and (promil <= 0.29):
            print("Blood alcohol concentration:", promil, '\n\n', b1)  
        elif (promil >= 0.30) and (promil <= 0.59):
            print("Blood alcohol concentration:", promil, '\n\n', b2)  
        elif (promil >= 0.60) and (promil <= 0.99):
            print("Blood alcohol concentration:", promil, '\n\n', b3)  
        elif (promil >= 1.00) and (promil <= 1.99):
            print("Blood alcohol concentration:", promil, '\n\n', b4)  
        elif (promil >= 2.00) and (promil <= 2.99):
            print("Blood alcohol concentration:", promil, '\n\n', b5)  
        elif (promil >= 3.00) and (promil <= 3.99):
            print("Blood alcohol concentration:", promil, '\n\n', b6)  
        elif (promil >= 4.00) and (promil <= 5.00):
            print("Blood alcohol concentration:", promil, '\n\n', b7)  
        elif (promil > 5.00):
            print("Blood alcohol concentration:", promil, '\n\n', b8)  

    if type_alc == 'b':
        kol_vo = int(input("""How much beer did you drink?
Note: 1 = one glass of 0.5 liters of beer 5.0% vol, etc. Your choice: """))
        massa = (kol_vo * 5.0) * 5
        promil = round ((massa / (weight * 0.7)), 2)

        if (promil >= 0) and (promil < 0.20):
            print("Blood alcohol concentration:", promil, "Not yet evening!")
        elif (promil >= 0.20) and (promil <= 0.29):
            print("Blood alcohol concentration:", promil, '\n\n', b1)  
        elif (promil >= 0.30) and (promil <= 0.59):
            print("Blood alcohol concentration:", promil, '\n\n', b2)  
        elif (promil >= 0.60) and (promil <= 0.99):
            print("Blood alcohol concentration:", promil, '\n\n', b3)  
        elif (promil >= 1.00) and (promil <= 1.99):
            print("Blood alcohol concentration:", promil, '\n\n', b4)  
        elif (promil >= 2.00) and (promil <= 2.99):
            print("Blood alcohol concentration:", promil, '\n\n', b5)  
        elif (promil >= 3.00) and (promil <= 3.99):
            print("Blood alcohol concentration:", promil, '\n\n', b6)  
        elif (promil >= 4.00) and (promil <= 5.00):
            print("Blood alcohol concentration:", promil, '\n\n', b7)  
        elif (promil > 5.00):
            print("Blood alcohol concentration:", promil, '\n\n', b8)  


if sex == 'w':
    print("""What type of alcohol did you drink?
Note: You can choose only one type of alcohol""")

    type_alc = input("Vine (type 'vn'), Beer (type 'b'). Yours choose is: ")
    print('\n')
      
    if type_alc == 'vn':
        kol_vo = int(input("""How much vine did you drink?
Note: 1 = 100 ml of vine with a strength of 16% vol, etc. Your choice: """))
        massa = kol_vo * 16.0
        promil = round ((massa / (weight * 0.6)), 2)
        
        if (promil >= 0) and (promil < 0.20):
            print("Blood alcohol concentration:", promil, "Not yet evening!")
        elif (promil >= 0.20) and (promil <= 0.29):
            print("Blood alcohol concentration:", promil, '\n\n', b1)  
        elif (promil >= 0.30) and (promil <= 0.59):
            print("Blood alcohol concentration:", promil, '\n\n', b2)  
        elif (promil >= 0.60) and (promil <= 0.99):
            print("Blood alcohol concentration:", promil, '\n\n', b3)  
        elif (promil >= 1.00) and (promil <= 1.99):
            print("Blood alcohol concentration:", promil, '\n\n', b4)  
        elif (promil >= 2.00) and (promil <= 2.99):
            print("Blood alcohol concentration:", promil, '\n\n', b5)  
        elif (promil >= 3.00) and (promil <= 3.99):
            print("Blood alcohol concentration:", promil, '\n\n', b6)  
        elif (promil >= 4.00) and (promil <= 5.00):
            print("Blood alcohol concentration:", promil, '\n\n', b7)  
        elif (promil > 5.00):
            print("Blood alcohol concentration:", promil, '\n\n', b8)  

    if type_alc == 'b':
        kol_vo = int(input("""How much beer did you drink?
Note: 1 = one glass of 0.5 liters of beer 5.0% vol, etc. Your choice: """))
        massa = (kol_vo * 5.0) * 5
        promil = round ((massa / (weight * 0.6)), 2)

        if (promil >= 0) and (promil < 0.20):
            print("Blood alcohol concentration:", promil, "Not yet evening!")
        elif (promil >= 0.20) and (promil <= 0.29):
            print("Blood alcohol concentration:", promil, '\n\n', b1)  
        elif (promil >= 0.30) and (promil <= 0.59):
            print("Blood alcohol concentration:", promil, '\n\n', b2)  
        elif (promil >= 0.60) and (promil <= 0.99):
            print("Blood alcohol concentration:", promil, '\n\n', b3)  
        elif (promil >= 1.00) and (promil <= 1.99):
            print("Blood alcohol concentration:", promil, '\n\n', b4)  
        elif (promil >= 2.00) and (promil <= 2.99):
            print("Blood alcohol concentration:", promil, '\n\n', b5)  
        elif (promil >= 3.00) and (promil <= 3.99):
            print("Blood alcohol concentration:", promil, '\n\n', b6)  
        elif (promil >= 4.00) and (promil <= 5.00):
            print("Blood alcohol concentration:", promil, '\n\n', b7)  
        elif (promil > 5.00):
            print("Blood alcohol concentration:", promil, '\n\n', b8)  
 
