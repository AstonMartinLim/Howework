test = True
result = test and 'Test is True' or 'Test is False'
print(result) # Test is True
print('\n')

# and возвращает нам 1-й False либо последний True
# т.к. при 1-м False выполнение кода прекращается
# чтобы вернулось True и слева и справа должно быть True, если слева True
# and проверяет условие справа, если там тоже True, возвращается последнее
# True
print(True and True) # True
print(False and True) # False
print(True and False) # False
print(False and False) # False
print(True and not True) # False
print(True and not False) # True
print(True is True) # True
# print(True in True) TypeError: argument of type 'bool' is not iterable

print('\n\n')

# or возвращает нам 1-й True или последний False 
# т.к. для истинности условия достаточно всего 1-го True (True нашел и условие
# дальше не выполняется). Последний False возращается т.к. ищет True до конца
print(True or True) # True
print(False or True) # True
print(True or False) # True
print(False or False) # False
print(True or not True) # True
