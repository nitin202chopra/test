price=int(input("enter price"))

quantity=int(input("enter qty"))


total=price*quantity

if quantity>=30:
    total=total-(total*30)/100
elif quantity>=20:
    total=total-(total*20)/100
elif quantity>=10:
    total=total-(total*10)/100




print("pay ",total)
