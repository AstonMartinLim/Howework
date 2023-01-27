# Умова задачі: Банкомат видає суму дрібними, але не більше 10 штук
# кожної дрібної купюри

print("ATM dispenses banknotes 10, 20, 50, 100, 200, 500, 1000")

money_wish = int(input("Type sum of money is you wish: "))

while money_wish > 0:
    if money_wish >= 10:
        counter_max = 10
        divisor = 0
        while counter_max > 0 and money_wish >= 10:
            counter_max -= 1
            divisor += 1
            counter = money_wish - 10
            money_wish = counter
        print("Банкомат выдаст", divisor, "купюр номиналом по 10$")
    
    if money_wish >= 20:
        counter_max = 10
        divisor = 0
        while counter_max > 0 and money_wish >= 20:
            counter_max -= 1
            divisor += 1
            counter = money_wish - 20
            money_wish = counter
        print("Банкомат выдаст", divisor, "купюр номиналом по 20$")
       
    if money_wish >= 50:
        counter_max = 10
        divisor = 0
        while counter_max > 0 and money_wish >= 50:
            counter_max -= 1
            divisor += 1
            counter = money_wish - 50
            money_wish = counter
        print("Банкомат выдаст", divisor, "купюр номиналом по 50$")
       
    if money_wish >= 100:
        counter_max = 10
        divisor = 0
        while counter_max > 0 and money_wish >= 100:
            counter_max -= 1
            divisor += 1
            counter = money_wish - 100
            money_wish = counter
        print("Банкомат выдаст", divisor, "купюр номиналом по 100$")
        
    if money_wish >= 200:
        counter_max = 10
        divisor = 0
        while counter_max > 0 and money_wish >= 200:
            counter_max -= 1
            divisor += 1
            counter = money_wish - 200
            money_wish = counter
        print("Банкомат выдаст", divisor, "купюр номиналом по 200$")
        
    if money_wish >= 500:
        counter_max = 10
        divisor = 0
        while counter_max > 0 and money_wish >= 500:
            counter_max -= 1
            divisor += 1
            counter = money_wish - 500
            money_wish = counter
        print("Банкомат выдаст", divisor, "купюр номиналом по 500$")
        
    if money_wish >= 1000:
        counter_max = 10
        divisor = 0
        while counter_max > 0 and money_wish >= 1000:
            counter_max -= 1
            divisor += 1
            counter = money_wish - 1000
            money_wish = counter
        print("Банкомат выдаст", divisor, "купюр номиналом по 1000$")
        
    if money_wish > 0:
        print("Остаток: ", money_wish, "$ был удержан т.к. закончились купюры!")
        break
