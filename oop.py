class Item:
    def calculate_the_price(self,x,y):
        return x*y


item1 = Item()
item1.name = 'phone'
item1.price = 500
item1.quantity = 5
print(item1.calculate_the_price(item1.price,item1.quantity))

item2 = Item()
item2.name = 'phone'
item2.price = 5000
item2.quantity = 6
print(item2.calculate_the_price(item2.price,item2.quantity))




