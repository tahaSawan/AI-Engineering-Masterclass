from abc import ABC,abstractmethod

class user(ABC):
    
    @abstractmethod
    def check_credentials(self,uname,passw):
        pass


class admin(user):

    def __init__(self,username,password):
        self.username=username
        self.password=password

    def check_credentials(self,uname,passw):

        if(self.username==uname and self.password==passw):
            return True 
        
        else:
            return False
        

class customer(user):

    def __init__(self,username,password):
        self.username=username
        self.password=password

    def check_credentials(self,uname,passw):

        if(self.username==uname and self.password==passw):
            return True 
        
        else:
            return False
        

class category:

    def __init__(self,cat1,cat2,cat3,id1,id2,id3):

        self.cat=cat1+","+cat2+","+cat3   # Category is a string separated by comma
        self.category_id=id1+","+id2+","+id3

    def display(self):

       cats = self.cat.split(",")
       ids = self.category_id.split(",")

       for c, i in zip(cats, ids):    #Learned it online
         print(f"{i} → {c}")

    
    def add_category(self,new_cat,new_cat_id):

        self.cat=self.cat+","+new_cat
        self.category_id=self.category_id+","+new_cat_id


    def delete_category(self, cat_name, cat_id):

        self.cat = self.cat.replace(cat_name, "").replace(",,", ",").strip(",")
        self.category_id = self.category_id.replace(cat_id, "").replace(",,", ",").strip(",")


    def modify_category(self,cat_name,cat_id,new_cat_name,new_cat_id):

        self.cat = self.cat.replace(cat_name, new_cat_name)
        self.category_id = self.category_id.replace(cat_id,new_cat_id)
    


    
class items:

    def __init__(self,
                 # Category 1 items
                 item1_id, item1_name, item1_cat, item1_price,
                 item2_id, item2_name, item2_cat, item2_price,
                 item3_id, item3_name, item3_cat, item3_price,

                 # Category 2 items
                 item4_id, item4_name, item4_cat, item4_price,
                 item5_id, item5_name, item5_cat, item5_price,
                 item6_id, item6_name, item6_cat, item6_price,

                 # Category 3 items
                 item7_id, item7_name, item7_cat, item7_price,
                 item8_id, item8_name, item8_cat, item8_price,
                 item9_id, item9_name, item9_cat, item9_price):

        self.items = (
            item1_id + "-" + item1_name + "-" + item1_cat + "-" + item1_price + "," +
            item2_id + "-" + item2_name + "-" + item2_cat + "-" + item2_price + "," +
            item3_id + "-" + item3_name + "-" + item3_cat + "-" + item3_price + "," +

            item4_id + "-" + item4_name + "-" + item4_cat + "-" + item4_price + "," +
            item5_id + "-" + item5_name + "-" + item5_cat + "-" + item5_price + "," +
            item6_id + "-" + item6_name + "-" + item6_cat + "-" + item6_price + "," +

            item7_id + "-" + item7_name + "-" + item7_cat + "-" + item7_price + "," +
            item8_id + "-" + item8_name + "-" + item8_cat + "-" + item8_price + "," +
            item9_id + "-" + item9_name + "-" + item9_cat + "-" + item9_price
        )

    
    def display(self):
        
        its=self.items.split(",")

        for i in its:
            print(f"{i}")
          
        
    def add_item(self,item_id,item_name,item_cat,item_price):

        self_items=self_items+","+item_id+"-"+item_name+"-"+item_cat+"-"+item_price

    def delete_item(self, item_id, item_name, item_cat, item_price):

        target = item_id + "-" + item_name + "-" + item_cat + "-" + item_price
        self.items = self.items.replace(target, "")
        self.items = self.items.replace(",,", ",").strip(",")

    def modify_item(self, old_id, old_name, old_cat, old_price,
                new_id, new_name, new_cat, new_price):
    
        old_item = old_id + "-" + old_name + "-" + old_cat + "-" + old_price
        new_item = new_id + "-" + new_name + "-" + new_cat + "-" + new_price
        self.items = self.items.replace(old_item, new_item)




if __name__ == "__main__":
    print("Welcome to the Demo Marketplace")

    admin_user = admin("admin", "admin123")
    customer_user = customer("customer", "cust123")
    categories = category("Clothing", "Footwear", "Electronics", "C1", "C2", "C3")
    it = items(
        "I1", "Sneakers", "C1", "2000",
        "I2", "Boots", "C1", "2500",
        "I3", "Slippers", "C1", "1000",
        "I4", "Shirt", "C2", "1500",
        "I5", "Jacket", "C2", "3000",
        "I6", "Jeans", "C2", "2000",
        "I7", "Phone", "C3", "50000",
        "I8", "Laptop", "C3", "120000",
        "I9", "Headphones", "C3", "5000"
    )

    print("Please login to continue:\n1. Yes\n2. No")
    choice = int(input("Choice: "))

    if choice == 1:
        print("Select Usertype:\n1. Admin\n2. Customer")
        utype = int(input("Usertype: "))

        # ------------------ ADMIN LOGIN ------------------
        if utype == 1:
            a = 0
            while a == 0:
                print("Enter username:")
                uname = input()
                print("Enter password:")
                passw = input()

                a = admin_user.check_credentials(uname, passw)

                if a:
                    print("Login Successful as Admin")
                    print("You can now manage the marketplace.")

                    while True:
                        print("\n--- Admin Menu ---")
                        print("1. View Categories")
                        print("2. View Items")
                        print("3. Add Category")
                        print("4. Delete Category")
                        print("5. Modify Category")
                        print("6. Add Item in a Category")
                        print("7. Delete Item in a Category")
                        print("8. Modify Item")
                        print("9. Logout")

                        admin_choice = int(input("Enter your choice: "))

                        if admin_choice == 1:
                            categories.display()

                        elif admin_choice == 2:
                            it.display()

                        elif admin_choice == 3:

                            print("Current Categories:")
                            categories.display()
                            a=input("Enter new category:")
                            b=input("Enter ID, must be new:")
                            categories.add_category(a,b)
                            print("Category added successfully")

                        elif admin_choice == 4:

                            print("Current Categories:")
                            categories.display()
                            a=input("Enter category to delete:")
                            b=input("Enter ID:")
                            categories.delete_category(a,b)
                            print("Category deleted successfully")

                        elif admin_choice == 5:

                            print("Current Categories:")
                            categories.display()
                            a=input("Enter category to modify:")
                            b=input("Enter ID:")
                            c=input("Enter modified category name:")
                            d=input("Enter new ID:")
                            categories.modify_category(a,b,c,d)

                            print("Category modified successfully")


                        elif admin_choice == 6:

                            print("Current Items")
                            it.display()
                            a=input("Enter item ID:")
                            b=input("Enter item name:")
                            c=input("Enter Category ID:")
                            d=input("Enter price:")
                            it.add_item()

                            print("Item added successfully!")

                        elif admin_choice == 7:
                            print("Current Items")
                            it.display()
                            a=input("Enter item ID:")
                            b=input("Enter item name:")
                            c=input("Enter Category ID:")
                            d=input("Enter price:")
                            it.delete_item()

                            print("Item Deleted Successfully")

                        elif admin_choice == 8:

                            print("Current Items")
                            it.display()
                            a=input("Enter old item ID:")
                            b=input("Enter old item name:")
                            c=input("Enter old Category ID:")
                            d=input("Enter old price:")

                            e=input("Enter new item ID:")
                            f=input("Enter new item name:")
                            g=input("Enter new Category ID:")
                            h=input("Enter new price:")

                            it.modify_item(a,b,c,d,e,f,g,h)

                        elif admin_choice == 9:
                            print("Logging out as Admin...")
                            break
                        else:
                            print("Invalid choice. Try again.")
                else:
                    print("Login Failed. Invalid credentials for Admin.")

        # ------------------ CUSTOMER LOGIN ------------------
        elif utype == 2:
            b = 0
            while b == 0:
                print("Enter username:")
                uname = input()
                print("Enter password:")
                passw = input()

                b = customer_user.check_credentials(uname, passw)

                if b:
                    print("Login Successful as Customer")
                    print("Happy Shopping!")

                    while True:
                        print("\n--- Customer Menu ---")
                        print("1. View Categories")
                        print("2. View Items")
                        print("3. Search Item by Name")
                        print("4. Logout")

                        cust_choice = int(input("Enter your choice: "))

                        if cust_choice == 1:
                            categories.view_categories()
                        elif cust_choice == 2:
                            it.view_items()
                        elif cust_choice == 3:
                            it.search_items()
                        elif cust_choice == 4:
                            print("Logging out as Customer...")
                            break
                        else:
                            print("Invalid choice. Try again.")
                else:
                    print("Login Failed. Invalid credentials for Customer.")
