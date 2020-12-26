usernameInput = input("Username : ")
passwordInput = input("Password : ")

if usernameInput == 'customer' and passwordInput == '1234':
    print("Login Success")
    print("--------- Seafood Shop ---------")
    print("Product                  Price")
    print("1.Crab                  100 THB")
    print("2.Shrimp                 50 THB")
    print("3.Shellfish              10 THB")
    print("4.Squid                  70 THB")
    print("5.Salmon                120 THB")
    print("6.Tuna                  150 THB")
    productSelected = int(input("Please select product (Number) : "))
    if productSelected == 1:
        amount = int(input("Amount : "))
        print("Product : Crab", "|", "Amount :", amount, "|", "Price :", amount * 100, "THB")
    elif productSelected == 2:
        amount = int(input("Amount : "))
        print("Product : Shrimp", "|", "Amount :", amount, "|", "Price :", amount * 50, "THB")
    elif productSelected == 3:
        amount = int(input("Amount : "))
        print("Product : Shellfish", "|", "Amount :", amount, "|", "Price :", amount * 10, "THB")
    elif productSelected == 4:
        amount = int(input("Amount : "))
        print("Product : Squid", "|", "Amount :", amount, "|", "Price :", amount * 70, "THB")
    elif productSelected == 5:
        amount = int(input("Amount : "))
        print("Product : Salmon", "|", "Amount :", amount, "|", "Price :", amount * 120, "THB")
    elif productSelected == 6:
        amount = int(input("Amount : "))
        print("Product : Tuna", "|", "Amount :", amount, "|", "Price :", amount * 150, "THB")
    else:
        print("Warning : Sorry you wrong fill in. ")
    print("----------------------------------")
    print("           Thank you           ")