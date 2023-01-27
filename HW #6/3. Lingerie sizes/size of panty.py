# Написати функцію переведення розмірів жіночої білизни з міжнародної у решту.
# Всередині функції потрібно просто звертатися до правильно складеного
# словника.


underwear_size = {
    'XXS': {'RU': 42, 'DE': 36, 'US': 8, 'FR': 38, 'GB': 24},
    'XS': {'RU': 44, 'DE': 34, 'US': 10, 'FR': 40, 'GB': 26},
    'S': {'RU': 46, 'DE': 40, 'US': 12, 'FR': 42, 'GB': 28},
    'M': {'RU': 48, 'DE': 42, 'US': 14, 'FR': 44, 'GB': 30},
    'L': {'RU': 50, 'DE': 44, 'US': 16, 'FR': 46, 'GB': 32},
    'XL': {'RU': 52, 'DE': 46, 'US': 18, 'FR': 48, 'GB': 34},
    'XXL': {'RU': 54, 'DE': 48, 'US': 20, 'FR': 50, 'GB': 36},
    'XXXL': {'RU': 56, 'DE': 50, 'US': 22, 'FR': 52, 'GB': 38},
    }

text1 = '''Ця программа здійснює переведення розмірів жіночої білизни з
            міжнародної (XXS, XS, S, M, L, XL, XXL, XXXL) у решту.'''

text2 = '''Примітка: можна використовувати лише літери верьхнього регістру,
           де RU - Росія, DE - Німечинна, US - США, FR - Франція,
           GB - Об'єднане королівство Великобританії та Північної Ірландії'''

print(f'{text1} \n', '**' * 38, '\n', f'{text2} \n')

international_size = input('Введіть міжнародний розмір білизни: ')
desired_size = input('''Введіть дві літери індекса країни для конвертації
розміру: ''')


def sizing (international_size, desired_size, underwear_size):
    for key, val in underwear_size.items():
        if key == international_size:
            for index in val:
                if desired_size == 'RU':
                    return val['RU']
                if desired_size == 'DE':
                    return val['DE']
                if desired_size == 'US':
                    return val['US']
                if desired_size == 'FR':
                    return val['FR']
                if desired_size == 'GB':
                    return val['GB']


result = sizing (international_size, desired_size, underwear_size)

print(f'''Розмір білизни за міжнародною класифікацією {international_size}
      дорівнює розміру {result} за класифікацією країни {desired_size}''')
