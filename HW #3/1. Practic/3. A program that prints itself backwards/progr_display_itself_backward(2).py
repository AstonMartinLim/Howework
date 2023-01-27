
# Написати програму, яка виводить саму себе задом наперед

# Вариант №2
# С использованием функции reversed ()
# П.С. результат не такой красивый как в варианте №1

import sys
filename = sys.argv[0]
# далі відкриваємо файл для читання (опція 'r')

f = open(filename, 'r', encoding='utf-8') # в файлі тепер file descriptor

for line in f: # для кожного рядка у файлі
        print(list(reversed(line)))
f.close() # закриття файлу
