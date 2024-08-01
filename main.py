
from datetime import datetime
from read import *
from operations import *
from write import *


contents = read()
print("\n")
print("*************************************************************************************")
print("\t \t \t \tWelcome to haven Laptops")
print("************************************************************************************")
print("\t \t Location: Kathmandu,chabahil Contact: 014421445,9800000000")
print("*************************************************************************************")
print("\n")

mainLoop = True 
while mainLoop == True:
    print("\n")
    print("Select 1 to purchase from manufacturer")
    print("Select 2 to sell the item")
    print("Select 3 to exit the System")
    user_options = 0
    try:
        user_options = int(input("Enter 1,2 or 3: "))
    except:
        print("please enter the appropriate number to use the program")
        continue
    
    
        
    if user_options == 1:
        today_date_and_time = datetime.now()
        name, number, user_purchased_laptops, vat_amount, final_total = purchase(contents)
        write_purchase(name, number, user_purchased_laptops, vat_amount, final_total)
            
    elif user_options == 2:
        
        name, number, user_purchased_laptops,grand_total = sell(contents)
        write_sell(name, number, user_purchased_laptops,grand_total)
    elif user_options == 3:
        mainLoop = False
        print("Thank You for visiting, for any inquries contact:980000000")
    else:
        print("Enter valid option")
