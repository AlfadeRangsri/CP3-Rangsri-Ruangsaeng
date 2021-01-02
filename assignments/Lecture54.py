def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == '1234':
        print("--------------------")
        print("   Login Success!")
        print("--------------------")
        showMenu()
    else:
        return "Username or Password in correct."


def showMenu():
    print("-----Alfred Shop-----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    menuSelect()


def menuSelect():
    userSelected = int(input("Select menu : "))
    if userSelected == 1:
        totalPrice = float(input("Please fill in price : "))
        print(vatCalculate(totalPrice), "Bath")
    elif userSelected == 2:
        print(priceCalculate(), "Bath")


def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result


def priceCalculate():
    price1 = int(input("First product price : "))
    price2 = int(input("Second product price : "))
    return vatCalculate(price1 + price2)


login()
