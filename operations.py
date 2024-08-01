from read import *
from datetime import datetime
def purchase(contents):  
    print("Thank you for purchaseing from manufacturer")
    print("=====================================================================================")
    print("We will need your name and phone number")
    name = input("Enter your name: ")
    number = input("Enter your number: ")
    print("=====================================================================================")

    print("S.N. \t Name \t\t Brand \t\t Price Quantity Processor \t Graphic Card")
    print("=====================================================================================")
    a = 1
    with open("Laptop.txt",'r') as file:
        for line in file:
            print(a,"\t" + line.replace(",","\t"))
            a +=1
        print("=====================================================================================")

        print("\n")
        ID_validation = 0
        try:
            ID_validation = int(input("Please provide the ID of the laptop you want to purchase: "))
        except:
            print("Enter a valid number!")
        while ID_validation<=0 or ID_validation>len(contents):
            print("Please provide a valid laptop ID!")
            print("\n")
            try:
                ID_validation = int(input("Please provide the ID of the laptop you want to purchase: "))
            except:
                print("Enter a number")

        quantity_validity = 0
        try:
            quantity_validity = int(input("Please provide the quantity of the laptop you want to purchase: "))
        except:
            print("Please provide the valid input.")
        get_quantity = contents[ID_validation][3]
        while quantity_validity<=0:
            print("\n")
            try:
                quantity_validity = int(input("Please provide the quantity of the laptop you want to purchase: "))
            except:
                print("Please provide the valid input.")

        contents[ID_validation][3] = int(contents[ID_validation][3]) + int(quantity_validity)
        with open("Laptop.txt","w") as file:
            for values in contents.values():
                file.write(str(values[0])+ "," + str(values[1]) + "," + str(values[2])+ "," + str(values[3])+ "," + str(values[4])+ "," + str(values[5]))
                file.write("\n")

        #Purchasing from manufacturer
        name_of_item = contents[ID_validation][0]
        user_selected_quantity = quantity_validity
        unit_cost = contents[ID_validation][2]
        selected_items_cost = contents[ID_validation][2].replace("$",'')
        total_cost = int(selected_items_cost)*int(user_selected_quantity)

        user_purchased_items = []
        user_purchased_items.append([name_of_item, user_selected_quantity, unit_cost, total_cost])

        vat_amount = total_cost * 0.13
        final_total = total_cost + vat_amount

        purchase_loop = True
    while purchase_loop == True:
        purchase = input("Do you want to purchase more laptops?(y/n):")
        if purchase == "y" or purchase == "Y":

            #Valid ID
            ID_validation = 0
            try:
                ID_validation = int(input("Please Provide the ID of the laptop you want to purchase:"))
                print("\n")
            except:
                print("Enter a number")
            
            while ID_validation <= 0 or ID_validation > len(contents):
                print("Please provide a valid Laptop ID !!")
                print("\n")
            
                try:
                    ID_validation = int(input("Please Provide the ID of the laptop you want to purchase:"))
                    print("\n")
                except:
                    print("Enter a number")

            user_desired_quantity = 0
            try:
                user_desired_quantity = int(input("Please Provide the number of quantity of the Laptop you want to purchase:"))
                print("\n")
            except:
                print("Please provide the valid input")

            while quantity_validity<=0:
                print("\n")
            try:
                quantity_validity = int(input("Please provide the quantity of the laptop you want to purchase: "))
            except:
                print("please provide the valid input")
            

           
            #Valid Quantity

            contents = read()
            get_quantity = contents[ID_validation][3]
            while user_desired_quantity <= 0 or user_desired_quantity > int(get_quantity):
                print("Dear Admin, the quantity you looking for is not available in our shop. Please look again in the Laptop screen")
                print("\n")

                try:
                    user_desired_quantity = int(input("Please Provide the number of quantity of the Laptop you want to purchase: "))
                    print("\n")
                except:
                    print("Please provide the valid input.")

            

            #Update the text file

            contents[ID_validation][3] = int(contents[ID_validation][3]) + int(user_desired_quantity)

            file = open("Laptop.txt","w")

            for values in contents.values():
                file.write(str(values[0])+"," +str(values[1])+"," +str(values[2])+"," +str(values[3])+"," +str(values[4])+"," +str(values[5]))
                file.write("\n")
            file.close()

            #Purchasing from manufacturer

            product_name = contents[ID_validation][0]
            brand_name = contents[ID_validation][1]
            quantity_of_user = user_desired_quantity
            price_of_unit = contents[ID_validation][2].replace("$","")
            final_price = int(price_of_unit)*int(quantity_of_user)

            final_total = final_total + final_price
            VAT = 0.13 * final_total
            total_with_vat = VAT + final_total
           
            user_purchased_items.append([product_name,brand_name, quantity_of_user, price_of_unit, final_price])
            
        else:
            purchase_loop = False

        today_date_and_time = datetime.now()
        print("\n")
        print("\t \t \t \t laptop shop bill ")
        print("\n")
        print("\t \t kamalpokhari, kathmandu | phone no: 9841324552")
        print("\n")
        print("----------------------------------------------------------------------")
        print("Laptop details are:")
        print("----------------------------------------------------------------------")
        print("Name of the Customers: " + str(name))
        print("Contact number: " + str(number))
        print("Date and time of purchase: " + str(today_date_and_time))
        print("----------------------------------------------------------------------")
        print("\n")
        print("Purchase Detail are:")
        print("----------------------------------------------------------------------")
        print("Item Name \t\t Unit Price \t\t\t Total")
        print("----------------------------------------------------------------------")
        for i in user_purchased_items:
            print(i[0],"\t\t\t",i[1],"\t\t\t",i[2],"\t\t\t","$",i[3])
        print("----------------------------------------------------------------------")
        print("Vat amount: "+ str(vat_amount))
        print("Grand total: "+str(final_total))

    return name, number, user_purchased_items, vat_amount, final_total

def sell(contents):
    print("Thank you for selling to customer")
    
    print("=====================================================================================")
    print("We will need your name and phone number")
    name = input("Enter your name: ")
    number = input("Enter your number: ")
    print("=====================================================================================")

    print("S.N. \t Name \t\t Brand \t\t Price Quantity Processor \t Graphic Card")
    print("=====================================================================================")
    a = 1
    with open("Laptop.txt",'r') as file:
        for line in file:
            print(a,"\t" + line.replace(",","\t"))
            a +=1
        print("=====================================================================================")

        print("\n")

        ID_validation = 0
        try:
            ID_validation = int(input("Please provide the ID of the laptop you want to Sell: "))
        except:
            print("Please provide the valid input.")

        while ID_validation<=0 or ID_validation>len(contents):
            print("Please provide a valid laptop ID!")
            print("\n")
            
            try:
                ID_validation = int(input("Please provide the ID of the laptop you want to Sell: "))
            except:
                    print("Please provide the valid input.")


        quantity_validity = 0
        try:
            quantity_validity = int(input("Please provide the quantity of the laptop you want to purchase: "))
            print("\n")
        except:
            print("Please provide the valid input.")
        

        get_quantity = contents[ID_validation][3]
        while quantity_validity<=0 or quantity_validity > int(get_quantity):
            print("Dear User, your desired laptop is out of stock, please retry later!")
            print("\n")

            try:
                quantity_validity = int(input("Please provide the quantity of the laptop you want to purchase: "))
                print("\n")
            except:
                print("Please provide the valid input.")

        contents[ID_validation][3] = int(contents[ID_validation][3]) - int(quantity_validity)
        with open("Laptop.txt","w") as file:
            for values in contents.values():
                file.write(str(values[0])+ "," + str(values[1]) + "," + str(values[2])+ "," + str(values[3])+ "," + str(values[4])+ "," + str(values[5]))
                file.write("\n")

        # Getting user purchased items
        name_of_item = contents[ID_validation][0]
        user_selected_quantity = quantity_validity
        unit_cost = contents[ID_validation][2]
        selected_items_cost = contents[ID_validation][2].replace("$",'')
        total_cost = int(selected_items_cost)*int(user_selected_quantity)

        user_purchased_items = []
        user_purchased_items.append([name_of_item, user_selected_quantity, unit_cost, total_cost])

        shipping_cost = input("Dear user do you want your laptop to be shipped?(Y/N)").upper()

        if shipping_cost == "Y":
            total = 0
            shipping_cost = 500
            for i in user_purchased_items:
                total += int(i[3])
            grand_total = total + shipping_cost

        else:
            total=0
            shipping_cost=0
            for i in user_purchased_items:
                total += int(i[3])
            grand_total = total + shipping_cost
        

        sale_loop = True
    while sale_loop == True:
        continue_sale = input("Do you want to purchase more laptops? (y/n) ").lower()
        if continue_sale == "y" or continue_sale == "yes":
            ID_validation = int(input("Please Provide the ID of the product you want to sell:"))
            print("\n")

            #Valid ID

            ID_validation = 0
            try:
                ID_validation = int(input("Please Provide the ID of the laptop you want to sell:"))
            except:
                print("Please provide the valid input")
            while ID_validation <= 0 or ID_validation > len(read()):
                print("Please provide a valid Laptop ID !!")
                try:
                    ID_validation = int(input("Please Provide the ID of the laptop you want to sell:"))
                except:
                    print("Please provide the valid input")
            user_desired_quantity =0
            try:   
                user_desired_quantity = int(input("Please Provide the number of quantity of the laptop you want to sell:"))
            except:
                print("Please provide the valid input.")
            while quantity_validity <= 0 or ID_validation > len(read()):
                print("please provide the valid input")
                try:
                    quantity_validity = int(input("Please Provide the ID of the laptop you want to sell:"))
                except:
                    print("please provide the valid input")
            #Valid Quantity

            contents = read()
            get_quantity = contents[ID_validation][3]
            while user_desired_quantity <= 0 or user_desired_quantity > int(get_quantity):
                print("Dear Admin, the quantity you looking for is not available in our shop. Please look again in the Laptop screen")
                print("\n")

                try:
                    user_desired_quantity = int(input("Please Provide the number of quantity of the Laptop you want to sell: "))
                    print("\n")
                except:
                    print("Please provide the valid input.")

            #Update the text file

            contents[ID_validation][3] = int(contents[ID_validation][3]) - int(user_desired_quantity)

            file = open("Laptop.txt","w")

            for values in contents.values():
                file.write(str(values[0])+"," +str(values[1])+"," +str(values[2])+"," +str(values[3])+"," +str(values[4])+"," +str(values[5]))
                file.write("\n")
            file.close()

            #getting user purchased items

            product_name = contents[ID_validation][0]
            brand_name = contents[ID_validation][1]
            quantity_of_user = user_desired_quantity
            #price_of_unit = contents[ID_validation][2]
            price_of_item = contents[ID_validation][2].replace("$",'')
            final_price = int(price_of_item)*int(quantity_of_user)
            final_total = 0

            user_purchased_items.append([product_name,brand_name, quantity_of_user, price_of_item, final_price])
            final_total = final_total + final_price
        else:
            sale_loop = False

        today_date_and_time = datetime.now()
        print("\n")
        print("\t \t \t \t laptop shop bill ")
        print("\n")
        print("\t \t kamalpokhari, kathmandu | phone no: 9841324552")
        print("\n")
        print("----------------------------------------------------------------------")
        print("Laptop details are:")
        print("----------------------------------------------------------------------")
        print("Name of the Customers: " + str(name))
        print("Contact number: " + str(number))
        print("Date and time of purchase: " + str(today_date_and_time))
        print("----------------------------------------------------------------------")
        print("\n")
        print("Purchase Detail are:")
        print("----------------------------------------------------------------------")
        print("Item Name \t\t Quantity \t\t Unit Price \t\t\t Total")
        print("----------------------------------------------------------------------")
        for i in user_purchased_items:
            print(i[0],"\t\t",i[1],"\t\t",i[2],"\t\t","$",i[3])
        print("----------------------------------------------------------------------")

        
        if shipping_cost=="Y":
            print("Your Shipping Cost is: ", shipping_cost)
            print("Grand Total: $"+str(grand_total))
            print("Note: Shipping cost is added to the grand total")
        else:
            print("Grand Total: $"+str(grand_total))
    return name, number, user_purchased_items,grand_total
