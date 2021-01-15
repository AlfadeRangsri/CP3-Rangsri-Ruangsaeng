from forex_python.converter import CurrencyRates

c = CurrencyRates()
currency_usd = c.get_rate('THB', 'USD')
currency_euro = c.get_rate('THB', 'EUR')
currency_japan = c.get_rate('THB', 'JPY')
# print(currency_rate.get_rate('USD', 'THB'))


total_price = 0
person_id = input('Username : ')
person_password = input('Password : ')
if person_id == 'customer' and person_password == '1150':
    print('         Login success')
    print('-'*32)
    print('     Welcome to Alfred shop !')
    print(' 1.  Cook book         100 THB')
    print(' 2.  Python book       300 THB')
    print(' 3.  Angular Book      300 THB')
    print(' 4.  OOP book          500 THB')
    print(' 5.  Javascript book   400 THB')
    print(' 6.  Django book       650 THB')
    print(' 7.  Fishing book      150 THB')
    print(' 8.  AI book          1500 THB')
    print(' 9.  Bitcoin book      700 THB')
    print(' 10. Database book     200 THB')
    print('-'*32)
    print('*Description : If you finish select item you can typing "done" for exit from menu item.')
    print('-'*32)

    while True:
        select_item = input('Please select item number : ')
        if select_item == '1':
            amount = int(input('Amount : '))
            print('Product : Cook book', '|', 'Amount :', amount, '|', 'Price :', amount * 100, 'THB')
            total_price += amount * 100
        elif select_item == '2':
            amount = int(input('Amount : '))
            print('Product : Python book', '|', 'Amount :', amount, '|', 'Price :', amount * 300, 'THB')
            total_price += amount * 300
        elif select_item == '3':
            amount = int(input('Amount : '))
            print('Product : Angular Book', '|', 'Amount :', amount, '|', 'Price :', amount * 300, 'THB')
            total_price += amount * 300
        elif select_item == '4':
            amount = int(input('Amount : '))
            print('Product : OOP book', '|', 'Amount :', amount, '|', 'Price :', amount * 500, 'THB')
            total_price += amount * 500
        elif select_item == '5':
            amount = int(input('Amount : '))
            print('Product : Javascript book', '|', 'Amount :', amount, '|', 'Price :', amount * 400, 'THB')
            total_price += amount * 400
        elif select_item == '6':
            amount = int(input('Amount : '))
            print('Product : Django book', '|', 'Amount :', amount, '|', 'Price :', amount * 650, 'THB')
            total_price += amount * 650
        elif select_item == '7':
            amount = int(input('Amount : '))
            print('Product : Fishing book', '|', 'Amount :', amount, '|', 'Price :', amount * 150, 'THB')
            total_price += amount * 150
        elif select_item == '8':
            amount = int(input('Amount : '))
            print('Product : AI book', '|', 'Amount :', amount, '|', 'Price :', amount * 1500, 'THB')
            total_price += amount * 1500
        elif select_item == '9':
            amount = int(input('Amount : '))
            print('Product : Bitcoin book', '|', 'Amount :', amount, '|', 'Price :', amount * 700, 'THB')
            total_price += amount * 700
        elif select_item == '10':
            amount = int(input('Amount : '))
            print('Product : Database book', '|', 'Amount :', amount, '|', 'Price :', amount * 200, 'THB')
            total_price += amount * 200
        elif select_item == 'done':
            break
        else:
            print('Item number is incorrect!')

    print('What currency do you want to pay in ?')
    print('1. Bath   -> THB')
    print('2. Dollar -> USD')
    print('3. Euro   -> EUR')
    print('4. Japan  -> JPY')
    select_currency = int(input('Please select currency (1-4) : '))
    if select_currency == 1:
        print('Total price is', total_price, 'Bath')
        print('Thank You !!')
    elif select_currency == 2:
        print('Total price is', "{:.2f}".format(total_price * currency_usd), 'Dollar')
        print('Thank You !!')
    elif select_currency == 3:
        print('Total price is', "{:.2f}".format(total_price * currency_euro), 'Euro')
        print('Thank You !!')
    elif select_currency == 4:
        print('Total price is', "{:.2f}".format(total_price * currency_japan), 'Yen')
        print('Thank You !!')
    else:
        print('Please select only 1-4 !')

else:
    print('Username or Password is incorrect')








