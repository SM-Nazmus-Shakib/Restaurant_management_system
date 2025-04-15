from fooditem import FoodItem
from menu import Menu
from users import Customer,Admin,Employee
from restuarant import Restuarant
from orders import Order

mamar_restuarant=Restuarant('Mamar Restu')
def admin_menu():
    name=input('Enter Your Name: ')
    email=input('Enter your Mail: ')
    phone=input('Enter Your Phone: ')
    address=input('Enter Your Address: ')
    admin=Admin(name=name,email=email,phone=phone,address=address)

    while True:
        print(f'Welcome {admin.name}')
        print('1.Add new Item')
        print('2.Add new Employee')
        print('3.View Employee')
        print('4.View Items')
        print('5.Delete Items')
        print('6.Exit')

        choice=int(input('Enter Your Choice: '))
        if choice==1:
            item_name=input('Enter Item Name')
            item_price=int(input('Enter Item Price'))
            item_quantity=int(input('Enter Item Quantity'))
            item=FoodItem(item_name,item_price,item_quantity)
            admin.add_new_item(mamar_restuarant,item)
        elif choice==2:
            name=input('Enter Emp Name: ')
            email=input('Enter Emp Mail: ')
            phone=input('Enter Emp Phone: ')
            address=input('Enter Emp Address: ')
            age=input('Enter Emp Age: ')
            salary=input('Enter Emp Salary: ')
            designation=input('Enter Designation:')
            admin.add_employee(name, phone, email, address,age,designation,salary)
        elif choice==3:
            admin.view_employee(mamar_restuarant)
        elif choice==4:
            admin.view_menu(mamar_restuarant)
        elif choice==5:
            item_name=input('Enter Item Name')
            admin.remove_item(mamar_restuarant,item_name)
        elif choice==6:
            break
        else:
            print('Invalid Choice!')

def customer_menu():
    name=input('Enter Your Name: ')
    email=input('Enter your Mail: ')
    phone=input('Enter Your Phone: ')
    address=input('Enter Your Address: ')
    customer=Customer(name=name,email=email,phone=phone,address=address)

    while True:
        print(f'Welcome {customer.name}')
        print('1.View Menu')
        print('2.Add item to cart')
        print('3.View cart')
        print('4.PayBill')
        print('5.Exit')

        choice=int(input('Enter Your Choice: '))
        if choice==1:
            customer.view_menu(mamar_restuarant)
        elif choice==2:
            item_name=input('Enter your Item: ')
            item_quantity=int(input('Enter item quantity: '))
            customer.add_to_cart(mamar_restuarant,item_name,item_quantity)
        elif choice==3:
            customer.view_cart()
        elif choice==4:
            customer.pay_bill()
        elif choice==5:
            break
        else:
            print('Invalid Choice!')

while True:
    print('Welcome!')
    print('1.Customer')
    print('2.Admin')
    print('3.Exit')
    
    choice=int(input('Enter Your Choice: '))
    if choice==1:
        customer_menu()
    elif choice==2:
         admin_menu()   
    elif choice==3:
         break
    else:
        print('Invalid Choice!')