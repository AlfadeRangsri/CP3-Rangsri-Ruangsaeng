class Customer:
    name = ''
    lastName = ''
    age = 0

    def addCart(self):
        print('Added product to ', self.name, self.lastName, "'s cart")

customer1 = Customer()
customer1.name = 'Alfred'
customer1.lastName = 'Rangsri'
customer1.addCart()

customer2 = Customer()
customer2.name = 'Kaeng'
customer2.lastName = 'Pattarapong'
customer2.addCart()

customer3 = Customer()
customer3.name = 'Pae'
customer3.lastName = 'Sangsom'
customer3.addCart()

customer4 = Customer()
customer4.name = 'Ling'
customer4.lastName = 'Tander'
customer4.addCart()