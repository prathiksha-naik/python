#A SHOP GIVE DISCOUNT OF 10% IF PURCHASED QUANTITY > 1000 PRINT TOTAL COST OF USER
print("enter the quantity")
quantity=int(input())
if quantity>1000:
        print("cost is",((quantity)-(.1*quantity)))
else:
        print("cost is",quantity)
