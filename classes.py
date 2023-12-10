

import csv as csv # Importing csv for exporting financial reports to CSV files
import matplotlib.pyplot as plt # Importing matplotlib for graphing

class Transaction:
    def __init__(self, product, quantity, type_of_transaction):
        self.product = product
        self.quantity = quantity
        self.type_of_transaction = type_of_transaction
    
    def get_budget_impact(self):    #Profit/Loss statement
        if self.type_of_transaction == "sale":
            return 1 * self.quantity * self.product.sale_price
        else:
            return -1 * self.quantity * self.product.vendor_price


class Product:
    def __init__(self, name, sale_price, vendor_price):
        self.name = name
        self.sale_price = sale_price
        self.vendor_price = vendor_price
        


class InventoryManager:
    def __init__(self):
        self.inventory = {}
    
    def inc_product(self, product, qty): # increases the quantity of a product (for restocking)
        self.inventory[product] += qty
    
    def dec_product(self, product, qty): # decreases the quanitiy of a product (for sale)
        self.inventory[product] -= qty

    def add_product(self, product):
        self.inventory[product] = 0 # Initialize the quantity to 0 


class FinancialRecord:
    def __init__(self):
        self.transactions = []
    
    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_revenue(self):
        revenue = 0
        for trans in self.transactions:
            impact = trans.get_budget_impact()
            if impact > 0:
                revenue += impact
        return revenue
    
    def get_costs(self):
        costs = 0
        for trans in self.transactions:
            impact = trans.get_budget_impact()
            if impact < 0:
                costs += -1 * impact
        return costs

    def get_profit(self):
        profit = 0
        for trans in self.transactions:
            profit += trans.get_budget_impact()
        return profit

    def get_financial_info(self):
        return {
            'sales': self.get_revenue(),
            'expenses': self.get_costs(),
            'profit': self.get_profit()
        }

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



class RSM:
    def __init__(self, products):
        # fixme, add list of products here
        self.products = products
        self.financial_record = FinancialRecord()
        self.inventory_manager = InventoryManager()
        for product in self.products:
            self.inventory_manager.add_product(product)
    
    def conduct_sale(self, product, qty):
        trans = Transaction(product, qty, "sale")
        self.financial_record.add_transaction(trans)
        self.inventory_manager.dec_product(product, qty)
        print(f"Sold {qty} {product.name} for {qty * product.sale_price}")
    
    def restock_product(self, product, qty):
        trans = Transaction(product, qty, "restock")
        self.financial_record.add_transaction(trans)
        self.inventory_manager.inc_product(product, qty)
        print(f"Restocked {qty} {product.name} for {qty * product.vendor_price}")

    def generate_report(self):
        report_generator = ReportGenerator(self.financial_record)
        print(report_generator.generate_financial_report())
        report_generator.export_to_csv('financial_report.csv')
        grapher = Grapher()
        grapher.plot_sales_vs_expenses(self.financial_record)
        