# 1. Sample
serial_number = [1, 2, 3, 4, 5]
position = ['director', 'accountant', 'driver', 'lawyer', 'manager']
salary = [3000.0, 2000.0, 1000.0, 2000.0, 800.0]

result = list(zip(serial_number, position, salary))
[print(i) for i in result]

# 2. Sample
goods = ['bread', 'milk', 'sausage']
price = [1.20, 2.30, 5.60]
discount = [0.2, 0.3, 0.25]
new_price = [x * y for x, y in zip(price, discount)]
result = tuple(zip(goods, new_price))
print(result)
