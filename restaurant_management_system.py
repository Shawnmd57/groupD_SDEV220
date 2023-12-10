#Program name: restaurant_management_system.py
#Author(s): Shawn Daumer, Dominic Szpak, Tejas Shastri
#Date last updated: 12/9/2023
#Purpose: Simulates a restaurant management system for Chik-fil-a, allowing the user to add products to an inventory,
# order stock, and generate financial reports with graphs.



# https://docs.python.org/3/library/tkinter.ttk.html

import csv as csv # Importing csv for exporting financial reports to CSV files
import matplotlib.pyplot as plt # Importing matplotlib for graphing
import tkinter as tk # Importing tkinter for GUI

from classes import Transaction, Product, InventoryManager, FinancialRecord, ReportGenerator, Grapher, RSM # Importing classes from classes.py



# initializing product instances 

#product(name, sale_price, vendor_price)
chicken_sandwich = Product('Chick-fil-A Chicken Sandwich', 3.05, 2.60)
chicken_sandwich_combo = Product('Chick-fil-A Chicken Sandwich Combo', 5.95, 4.00)
chicken_deluxe_sandwich = Product('Chick-fil-A Chicken Deluxe Sandwich', 3.65, 2.50)
chicken_deluxe_sandwich_combo = Product('Chick-fil-A Chicken Deluxe Sandwich Combo', 6.55, 5.10)
spicy_chicken_sandwich = Product('Spicy Chicken Sandwich', 3.29, 3.00)
spicy_chicken_sandwich_combo = Product('Spicy Chicken Sandwich Combo', 6.19, 5.90)
spicy_chicken_deluxe_sandwich = Product('Spicy Chicken Deluxe Sandwich', 3.89, 3.45)
spicy_chicken_deluxe_sandwich_combo = Product('Spicy Chicken Deluxe Sandwich Combo', 6.79, 5.50)
nuggets_8pc = Product('Chick-fil-A Nuggets 8 Pc.', 3.05, 2.62)
nuggets_12pc = Product('Chick-fil-A Nuggets 12 Pc.', 4.45, 4.04)
nuggets_combo_8pc = Product('Chick-fil-A Nuggets Combo 8 Pc.', 5.95, 5.08)
nuggets_combo_12pc = Product('Chick-fil-A Nuggets Combo 12 Pc.', 8.59, 8.00)
nuggets_grilled_8pc = Product('Chick-fil-A Nuggets (Grilled) 8 Pc.', 3.85, 2.60)
nuggets_grilled_12pc = Product('Chick-fil-A Nuggets (Grilled) 12 Pc.', 5.75, 5.00)
nuggets_grilled_combo_8pc = Product('Chick-fil-A Nuggets (Grilled) Combo 8 Pc.', 6.75, 5.90)
nuggets_grilled_combo_12pc = Product('Chick-fil-A Nuggets (Grilled) Combo 12 Pc.', 8.59, 8.00)
strips_3pc = Product('Chick-n-Strips 3 Pc.', 3.35, 2.99)
strips_4pc = Product('Chick-n-Strips 4 Pc.', 4.39, 3.89)
strips_combo_3pc = Product('Chick-n-Strips Combo 3 Pc.', 6.25, 5.36)
strips_combo_4pc = Product('Chick-n-Strips Combo 4 Pc.', 7.25, 7.03)
grilled_chicken_sandwich = Product('Grilled Chicken Sandwich', 4.39, 4.10)
grilled_chicken_sandwich_combo = Product('Grilled Chicken Sandwich Combo', 7.19, 6.49)
grilled_chicken_club_sandwich = Product('Grilled Chicken Club Sandwich', 5.59, 4.34)
grilled_chicken_club_sandwich_combo = Product('Grilled Chicken Club Sandwich Combo', 8.39, 7.76)
chicken_salad_sandwich = Product('Chicken Salad Sandwich', 3.99, 2.55)
chicken_salad_sandwich_combo = Product('Chicken Salad Sandwich Combo', 6.79, 5.56)
grilled_chicken_cool_wrap = Product('Grilled Chicken Cool Wrap', 5.19, 4.50)
grilled_chicken_cool_wrap_combo = Product('Grilled Chicken Cool Wrap Combo', 8.15, 7.56)
soup_salad = Product('Soup & Salad (Large Chicken Soup and Side Salad)', 8.35, 7.78)
chilled_grilled_chicken_sub = Product('Chilled Grilled Chicken Sub Sandwich', 4.79, 4.30)
waffle_fries = Product('Waffle Fries', 1.99, 1.00)
small_soft_drink = Product('Small Soft Drink', 1.35, 0.20)
medium_soft_drinks = Product('Medium Soft Drinks', 1.59, 0.40)
large_soft_drinks = Product('Large Soft Drinks', 1.85, 0.80)



# Initialize inventory manager
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


RSM = RSM(products)
