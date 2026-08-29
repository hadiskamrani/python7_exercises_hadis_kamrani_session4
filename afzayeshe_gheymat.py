price = [5000,6000,7000,8000]
new_price = []
for i in price:
    i = i + (i *10/100)
    new_price.append(i)
print(new_price)