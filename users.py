from abc import ABC
from orders import Order
class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name=name
        self.email=email
        self.address=address
        self.phone=phone

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        
    def add_employee(self,restuarant,employee):
        restuarant.add_employee(employee)

    def view_employee(self,restuarant):
        restuarant.view_employee()

    def add_new_item(self,restuarant,item):
        restuarant.menu.add_new_item(item)
    def remove_item(self,restuarant,item):
        restuarant.menu.remove_item(item)
    
    def view_menu(self,restuarant):
        restuarant.menu.show_menu()

class Employee(User):
    def __init__(self, name, phone, email, address,age,designation,salary):
        self.age=age
        self.designation=designation
        self.salary=salary
        super().__init__(name, phone, email, address)


class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart=Order()

    def view_menu(self,restuarant):
        restuarant.menu.show_menu()
    
    def add_to_cart(self,restuatant,item_name,quantity):
        item=restuatant.menu.find_item(item_name)
        if item:
            item.quantity=quantity
            self.cart.add_item(item)
            print('Item Added')
        else:
            print('Item not found!')
    
    def view_cart(self):
        print('***View Cart***')
        print('Name\tPrice\tQuantity')
        for item,quantity in self.cart.items.items():
            print(f"{item.name} {item.price} {item.quantity}")
        print(f'Total price: {self.cart.total_price()}')
    
    def pay_bill(self):
        print(f'Total {self.cart.total_price} payment successful')
        self.cart.clear()


    





    
        



