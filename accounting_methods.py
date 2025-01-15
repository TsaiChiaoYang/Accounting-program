import os
import csv
class Accounting:
    def __init__(self):
        pass
    
    def file_path(self, date_list):
        """
        This is a helper method that returns the path of the file.
        
        Args:
            month (int): The month of the record 
            year (int): The year of the record
    
        Returns:
            str: The path of the file
        """
        # create a folder called data if it does not exist
        if not os.path.exists("data"):
            os.makedirs("data")
            
        # get the current date
        month = date_list[0]
        year = date_list[1]
        return f"data/{month}_{year}_accounting.csv"
    
    def read_accounting_file(self):
        """
        This is a method that prints out the accounting record of a certain month.
  
        Args:
            month (int): The month of the record 
            year (int): The year of the record
        """
        # get the current date
        date_list = self.get_current_date()
        path = self.file_path(date_list)
        try:
            with open(path, "r", encoding="utf-8") as file:
                # check if the file is empty
                lines = csv.reader(file)
                if lines == []:
                    print("The file is empty.")
                    return
                
                total_width = 80
                # devide the width into four sections (int), sw = section width
                sw = total_width // 4
                print(f"{'category' :<{sw}}{'name' :<{sw}}{'price' :<{sw}}{'time' :<{sw}}")
                for line in lines:
                    item_category, item_name, item_price, purchase_time = line[0], line[1], line[2], line[3]
                    print(f"{item_category :<{sw}}{item_name :<{sw}}{item_price :<{sw}}{purchase_time :<{sw}}")
        except FileNotFoundError:
            with open(path, "w", encoding="utf-8") as file:
                print("The file is empty.")
    
    def add_list_to_file(self, item_list):
        """ 
        This method write the details of the item to the file

        Args:
            month (int): The month of the detail
            year (int): The year of the detail
            item_list (list): The list which contains the detail of the item
        """
        # get the current date
        date_list = self.get_current_date()
        path = self.file_path(date_list)
        
        try:
            # if the file does not exist, create a new file
            with open(path, "x",encoding="utf-8") as file:
                # add the item to the file
                file.write(f"{item_list[0]},{item_list[1]},{item_list[2]},{item_list[3]}\n")
        except FileExistsError:
            # if the file already exists, add the item to the file
            with open(path, "a", encoding="utf-8") as file:
                file.write(f"{item_list[0]},{item_list[1]},{item_list[2]},{item_list[3]}\n")
        
        print("Accounting successful!")

    def choose_detail(self):
        """
        This is a method that allows the user to choose the details of the item.

        Returns:
            list: The list of the details of the item
        """
        category_list = ["food", "transportation", "entertainment", "others", "rent", "income", "daily_necessities", "insurance", "eating_out"]
        print("category: ")
        index = 1
        for category in category_list:
            print(f"\t{index}----{category}")
            index += 1
            
        category = input("category> ")
        item = input("name> ")
        price = input("price> ")
        date = input("date> ")
    
        detail_list = [category_list[int(category) - 1], item, price, date]
        return detail_list
    
    def set_current_date(self):
        """
        This is a method that allows the user to change the date of the record.
        
        Args:
            month (int): The month of the record 
            year (int): The year of the record
    
        Returns:
            tuple: The tuple of the month and year
        """
        month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        year_list = [2024, 2025, 2026, 2027, 2028, 2029, 2030]
        
        print("month: ")
        index = 1
        for month in month_list:
            print(f"\t{index}----{month}")
            index += 1
        month = input("> ")
        print()
        
        print("year: ")
        index = 1
        for year in year_list:
            print(f"\t{index}----{year}")
            index += 1
        year = input("> ")
        print()
        

        with open("record/current_date.txt", "w") as file:
            file.write(f"{month_list[int(month) - 1]} {year_list[int(year) - 1]}")

        
    def get_current_date(self):
        """
        This is a helper method that reads the current date.

        Returns:
            str: The current date
        """
        with open("record/current_date.txt", "r") as file:
            date_list = file.read().split()
            if date_list == []:
                print("The current date is not set.")
                print("Please enter the current date: ")
                self.set_current_date()
                return
        return date_list