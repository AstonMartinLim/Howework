# Написати програму, яка виводить сама себе

# Так же добавил encoding 3-м параметром в ф-ю open() чтобы небыло крякозябликов
# P.S. прогр. работает и в таком виде (как было дано в лекции)
# f = open(filename, 'r')

import sys
filename = sys.argv[0]
# далі відкриваємо файл для читання (опція 'r')
f = open(filename, 'r', encoding='utf-8') # в файлі тепер file descriptor
for line in f: # для кожного рядка у файлі
	print(line)
f.close() # закриття файлу
