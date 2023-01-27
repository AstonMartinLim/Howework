# Умова задачі: Банкомат видає суму максимально можливими купюрами

print("ATM dispenses banknotes 50, 100, 200, 500, 1000")

money_wish = int(input("Type sum of money is you wish: "))

# Использую цикл while для проверки условия, что введенная сумма больше 0 
while money_wish > 0:
    if money_wish >= 1000: # определяю money_wish > или == 1000
        divisor = money_wish // 1000 # определяю ск. раз money_wish делится без остатка на 1000
        counter = money_wish - divisor * 1000 # считаю остаток
        money_wish = counter # присваюваю остаток в перем. money_wish для последующей обработки по цепочке
        print("Банкомат выдаст", divisor, "купюр номиналом по 1000$")

    if money_wish >= 500: # определяю money_wish > или == 500
        divisor = money_wish // 500 # определяю ск. раз money_wish делится без остатка на 500
        counter = money_wish - divisor * 500 # считаю остаток
        money_wish = counter # присваюваю остаток в перем. money_wish для последующей обработки по цепочке
        print("Банкомат выдаст", divisor, "купюр номиналом по 500$")

    if money_wish >= 200: # определяю money_wish > или == 200
        divisor = money_wish // 200 # определяю ск. раз money_wish делится без остатка на 200
        counter = money_wish - divisor * 200 # считаю остаток
        money_wish = counter # присваюваю остаток в перем. money_wish для последующей обработки по цепочке
        print("Банкомат выдаст", divisor, "купюр номиналом по 200$")

    if money_wish >= 100: # определяю money_wish > или == 100
        divisor = money_wish // 100 # определяю ск. раз money_wish делится без остатка на 100
        counter = money_wish - divisor * 100 # считаю остаток
        money_wish = counter # присваюваю остаток в перем. money_wish для последующей обработки по цепочке
        print("Банкомат выдаст", divisor, "купюр номиналом по 100$")

    if money_wish >= 50: # определяю money_wish > или == 50
        divisor = money_wish // 50 # определяю ск. раз money_wish делится без остатка на 50
        counter = money_wish - divisor * 50 # считаю остаток
        money_wish = counter # присваюваю остаток в перем. money_wish для последующей обработки по цепочке
        print("Банкомат выдаст", divisor, "купюр номиналом по 50$")

    if money_wish > 0 and money_wish < 50: # определяю money_wish > 0 и < 50 (для ситуаций с остатком меньше 50
        # чтобы цикл while с условием money_wish > 0 не стал вечным
        print("Банкнот, номиналом меньше 50 нет, но мы списали выдачу:", money_wish, "$")
        break # разрав цикла для ситуаций с остатком
