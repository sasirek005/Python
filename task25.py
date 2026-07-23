n = int(input("Enter the number of days: "))
price = []
for i in range(n):
    num = int(input("Enter stock price: "))
    price.append(num)
min_price = price[0]
max_profit = 0
for i in range(1, n):
    if price[i] < min_price:
        min_price = price[i]
    profit = price[i] - min_price
    if profit > max_profit:
        max_profit = profit
print("Maximum profit:", max_profit)
