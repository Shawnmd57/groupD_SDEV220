#Program name: restaurant_management_system.cpp
#Author(s): Shawn Daumer, Dominic Szpak, Tejas Shastri
#Date last updated: 2/12/2023
#Purpose: Simulates a restaurant management system for Chik-fil-a that allows the user to add products to an inventory,
# order stock, and generate financial reports.


#***This version of the program does not yet have a GUI.***

import csv
import matplotlib.pyplot as plt


# ******Classes******
class Product:  # Class for product information
    def __init__(self, name, price, quantity): 
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_product(self, price, quantity): # Method for updating product information (quantity and price)
        self.price = price
        self.quantity += quantity

    def get_product_info(self): # Method for getting product information upon request
        return {'name': self.name, 'price': self.price, 'quantity': self.quantity}



class InventoryManager:
    def __init__(self):
        self.inventory = {} # Dictionary for storing product information

    def add_product(self, product): # Method for adding a product to the inventory
        if product.name in self.inventory:
            self.inventory[product.name].quantity += product.quantity
        else:
            self.inventory[product.name] = product

    def order_stock(self, product_name, additional_quantity):   # Increase the stock quantity of a product
        if product_name in self.inventory:
            self.inventory[product_name].quantity += additional_quantity
            print(f"Ordered {additional_quantity} more of {product_name}.")
        else:
            print(f"Error: {product_name} is not in the inventory.")

    def get_inventory(self):    # Return a summary of the inventory
        return {name: {'price': product.price, 'quantity': product.quantity} for name, product in self.inventory.items()}


class FinancialRecord:  # Class for managing financial records
    def __init__(self):
        self.expenses = 0
        self.sales = 0

    def record_sale(self, amount):  # Record a sale
        self.sales += amount

    def record_expense(self, amount):  # Record an expense
        self.expenses += amount

    def get_financial_info(self): # Return a summary of the financial information
        return {'expenses': self.expenses, 'sales': self.sales}


class ReportGenerator:  # Class for generating reports 
    def __init__(self, financial_record):
        self.financial_record = financial_record

    def generate_financial_report(self):    # Generate a financial report
        financial_info = self.financial_record.get_financial_info()
        return f"Total Sales: {financial_info['sales']} - Total Expenses: {financial_info['expenses']}"
    
    def export_to_csv(self, filename):  # Export the financial report to a CSV file
        financial_info = self.financial_record.get_financial_info()
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Total Sales', 'Total Expenses'])
            writer.writerow([financial_info['sales'], financial_info['expenses']])


class Grapher:  # Class for generating graphs
    def plot_sales_vs_expenses(self, financial_record):
        financial_info = financial_record.get_financial_info()
        labels = ['Sales', 'Expenses']
        sizes = [financial_info['sales'], financial_info['expenses']]
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.show()




# ---  Test Space  --- # 



# initializing product instances 
chicken_sandwich = Product('Chick-fil-A Chicken Sandwich', 3.05, 0)
chicken_sandwich_combo = Product('Chick-fil-A Chicken Sandwich Combo', 5.95, 0)
chicken_deluxe_sandwich = Product('Chick-fil-A Chicken Deluxe Sandwich', 3.65, 0)
chicken_deluxe_sandwich_combo = Product('Chick-fil-A Chicken Deluxe Sandwich Combo', 6.55, 0)
spicy_chicken_sandwich = Product('Spicy Chicken Sandwich', 3.29, 0)
spicy_chicken_sandwich_combo = Product('Spicy Chicken Sandwich Combo', 6.19, 0)
spicy_chicken_deluxe_sandwich = Product('Spicy Chicken Deluxe Sandwich', 3.89, 0)
spicy_chicken_deluxe_sandwich_combo = Product('Spicy Chicken Deluxe Sandwich Combo', 6.79, 50)
nuggets_8pc = Product('Chick-fil-A Nuggets 8 Pc.', 3.05, 0)
nuggets_12pc = Product('Chick-fil-A Nuggets 12 Pc.', 4.45, 0)
nuggets_combo_8pc = Product('Chick-fil-A Nuggets Combo 8 Pc.', 5.95, 0)
nuggets_combo_12pc = Product('Chick-fil-A Nuggets Combo 12 Pc.', 8.59, 0)
nuggets_grilled_8pc = Product('Chick-fil-A Nuggets (Grilled) 8 Pc.', 3.85, 0)
nuggets_grilled_12pc = Product('Chick-fil-A Nuggets (Grilled) 12 Pc.', 5.75, 0)
nuggets_grilled_combo_8pc = Product('Chick-fil-A Nuggets (Grilled) Combo 8 Pc.', 6.75, 0)
nuggets_grilled_combo_12pc = Product('Chick-fil-A Nuggets (Grilled) Combo 12 Pc.', 8.59, 0)
strips_3pc = Product('Chick-n-Strips 3 Pc.', 3.35, 0)
strips_4pc = Product('Chick-n-Strips 4 Pc.', 4.39, 0)
strips_combo_3pc = Product('Chick-n-Strips Combo 3 Pc.', 6.25, 0)
strips_combo_4pc = Product('Chick-n-Strips Combo 4 Pc.', 7.25, 0)
grilled_chicken_sandwich = Product('Grilled Chicken Sandwich', 4.39, 0)
grilled_chicken_sandwich_combo = Product('Grilled Chicken Sandwich Combo', 7.19, 0)
grilled_chicken_club_sandwich = Product('Grilled Chicken Club Sandwich', 5.59, 0)
grilled_chicken_club_sandwich_combo = Product('Grilled Chicken Club Sandwich Combo', 8.39, 0)
chicken_salad_sandwich = Product('Chicken Salad Sandwich', 3.99, 0)
chicken_salad_sandwich_combo = Product('Chicken Salad Sandwich Combo', 6.79, 0)
grilled_chicken_cool_wrap = Product('Grilled Chicken Cool Wrap', 5.19, 0)
grilled_chicken_cool_wrap_combo = Product('Grilled Chicken Cool Wrap Combo', 8.15, 0)
soup_salad = Product('Soup & Salad (Large Chicken Soup and Side Salad)', 8.35, 0)
chilled_grilled_chicken_sub = Product('Chilled Grilled Chicken Sub Sandwich', 4.79, 0)
waffle_fries = Product('Waffle Fries', 1.99, 0)
small_soft_drink = Product('Small Soft Drink', 1.35, 0)
medium_soft_drinks = Product('Medium Soft Drinks', 1.59, 0)
large_soft_drinks = Product('Large Soft Drinks', 1.85, 0)



# Initialize inventory manager
inventory_manager = InventoryManager()
products = [
    chicken_sandwich, chicken_sandwich_combo, chicken_deluxe_sandwich, chicken_deluxe_sandwich_combo,
    spicy_chicken_sandwich, spicy_chicken_sandwich_combo, spicy_chicken_deluxe_sandwich,
    spicy_chicken_deluxe_sandwich_combo, nuggets_8pc, nuggets_12pc, nuggets_combo_8pc, nuggets_combo_12pc,
    nuggets_grilled_8pc, nuggets_grilled_12pc, nuggets_grilled_combo_8pc, nuggets_grilled_combo_12pc,
    strips_3pc, strips_4pc, strips_combo_3pc, strips_combo_4pc, grilled_chicken_sandwich,
    grilled_chicken_sandwich_combo, grilled_chicken_club_sandwich, grilled_chicken_club_sandwich_combo,
    chicken_salad_sandwich, chicken_salad_sandwich_combo, grilled_chicken_cool_wrap,
    grilled_chicken_cool_wrap_combo, soup_salad, chilled_grilled_chicken_sub, waffle_fries,
    small_soft_drink, medium_soft_drinks, large_soft_drinks
]

# Add all the products to the inventory
for product in products:
    inventory_manager.add_product(product)

    # Print the inventory summary
inventory_summary = inventory_manager.get_inventory()
for product_name, info in inventory_summary.items():
    print(f"Product: {product_name}, Price: {info['price']}, Quantity: {info['quantity']}")

# Order more stock for a specific product
inventory_manager.order_stock('Waffle Fries', 100)

# Record financial transactions
financial_record = FinancialRecord()
financial_record.record_sale(500)   # A sale of $500
financial_record.record_expense(150) # An expense of $150

# Generate a report and export to CSV
report_generator = ReportGenerator(financial_record)
print(report_generator.generate_financial_report())
report_generator.export_to_csv('financial_report.csv')

# Create a graph for visualizing sales vs. expenses
grapher = Grapher()
grapher.plot_sales_vs_expenses(financial_record)