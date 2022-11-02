from data import shopping_cart
from add import add
from delete import delete
from add import user_dic

class ItemList:
    def __init__(self):
        self.question_number = 0
    
    def list_display(self):
        print('-' * 25)
        print("Welcome to Shopping Mart.")
        print('-' * 25)
        for i in range(0, len(shopping_cart)):
            self.question_number += 1
            print(
                f"{self.question_number}. {shopping_cart[i]['item']} - ${shopping_cart[i]['price']}")
   
        still_continue = True
        while still_continue:
            user_item = input("Select your Favourite Item From the Cart: ")
            if str("\'"+user_item+"\'") not in str(shopping_cart):
                print(f"{user_item} not included in Cart. please enter valid items")
                y = input("Do you want to leave(y/n)?").lower()
                if y == "y":
                    still_continue = False

                continue
            user_quantity = int(input(f"{user_item} quantity?: "))
            add(user_item, user_quantity)
            decision = input("You need to Add(a)/Delete(d)/Exit(e) : ").lower()
            
            if decision == 'd':
                item = input("Select delete Item: ")
                quantity = int(input(f"{item} quantity to remove : "))
                delete(item, quantity)
                still_continue = False

            if decision == "e": 
                still_continue = False
            
            if decision != "e" and decision != 'a':
                still_delete = True
                while still_delete:
                    x = input("Still need to remove from cart(y/n): ")
                    if x == 'y':
                        item = input("Select delete Item: ")
                        quantity = int(input(f"{item} quantity to remove : "))
                        delete(item, quantity)
                    if x == "n":
                        still_delete = False


      
                



            



        