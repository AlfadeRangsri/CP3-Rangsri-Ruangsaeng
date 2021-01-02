menuList = []
priceList = []

while True:
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == 'exit':
        break
    else:
        menuPrice = input("Price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)

def showBill():
    total = 0
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
        total += int(priceList[number])
    print("Total : ", total)

showBill()
