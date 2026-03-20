# coffee.py
coffee = 10
while True:
    money = int(input("put money:"))
    if money == 300:
        print("I give you a cup of coffee.")
        coffee -= 1
    elif money > 300:
        print("I give you a cupt of coffee. Money in change is %d." % (money-300))
        coffee -= 1
    else:
        print("Less money.. I don't give you a cup of coffee.")
        print("Remained cups of coffee is %d." % (coffee))
    if coffee == 0:
        print("We ran out of coffee. Stop sales.")
        break
