import os
from time import sleep
from accounting_methods import Accounting

accounting = Accounting()

exit = False
while exit == False:
    os.system("cls")
    print("Hello!")
    print("Press:")
    print("\t1----start accounting")
    print("\t2----view accounting files")
    print("\texit----exit")
    action = input(">")
    
    # start accounting
    if action == "1":
        exit_accounting = False
        while exit_accounting == False:
            sleep(0.5)
            os.system("cls")
            print(f"current date: {accounting.get_current_date()[0]} {accounting.get_current_date()[1]}")
            print()
            accounting.read_accounting_file()
            print()
            
            # detail of the item
            print("What do you want to account?")
            item_list = accounting.choose_detail()
            accounting.add_list_to_file(item_list)
            


            
    elif action == "2":
        # view accounting files
        exit = False
        while exit == False:

            print("which record do you want to view?")
            print("(type 'c' to change date)")
            print("(type 'q' to quit)")
    
            month = input("month: ")
            if month == 'c':
                break
            if month == 'q':
                break
            year = input("year: ")
            print()
            accounting.read_accounting_file(month, year)
            
    elif action == "exit":
        exit = True
