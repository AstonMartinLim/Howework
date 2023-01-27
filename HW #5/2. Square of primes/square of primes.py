# Написати функцію, яка буде підносити число у квадрат.
# Написати другу, яка буде перевіряти, чи є число простим.
# Потрібно видрукувати в головній програмі квадрати усіх простих чисел
# зі списку від 0 до 50 за допомогою map

def square(num):
    return num * num

def is_simple(num):
    for i in range(2, int(num**0.5)+1):
        if not num % i:
            return False
    return True

simple_list = list(filter(is_simple, range(51)))
print(list(map(square, simple_list)))
