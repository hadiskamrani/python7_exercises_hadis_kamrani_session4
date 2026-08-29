price = float(input("gheymat ra vared konid :"))
if price>=1000000:
    new_price = price - (price *20/100)
    print(new_price)
elif 500000<=price<1000000:
    new_price = price - (price *15/100)
    print(new_price)
elif price<500000:
    new_price = price - (price *10/100)
    print(new_price)