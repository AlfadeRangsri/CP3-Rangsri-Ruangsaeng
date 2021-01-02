systemMenu = {"fish": 50, "dog": 30, "cat": 40}
menuList = []

while True:
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == 'exit':
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])

def showBill():
    total = 0
    print("----- Alfred Food -----")
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])
        total += menuList[number][1]
    print("Total :", total)

showBill()