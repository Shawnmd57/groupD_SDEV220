# Hello world using the ttk sublibrary of tkinter
from tkinter import *
from tkinter import ttk
from restaurant_management_system import *


def conduct_pos_transaction(): 
    sale_window = Toplevel(root)
    sale_window.grid()
    names_lst = []
    for product in RSM.products:
        names_lst.append(product.name)
    combobox = ttk.Combobox(sale_window, values=names_lst)
    combobox.grid(column=0, row=0)
    # entery box for quantity of product
    quantity = ttk.Entry(sale_window)
    quantity.grid(column=1, row=0)

    def confirm_pos_trans():
        prod = None
        for product in RSM.products:
            if product.name == combobox.get():
                prod = product
        quan = int(quantity.get())
        RSM.conduct_sale(prod, quan)
    ttk.Button(sale_window, text="Confirm Order", command=confirm_pos_trans).grid(column=2, row=0)



def conduct_restock_transaction():
    restock_window = Toplevel(root)
    restock_window.grid()
    names_lst = []
    for product in RSM.products:
        names_lst.append(product.name)
    combobox = ttk.Combobox(restock_window, values=names_lst)
    combobox.grid(column=0, row=0)
    # entery box for quantity of product
    quantity = ttk.Entry(restock_window)
    quantity.grid(column=1, row=0)

    def confirm_restock_trans():
        prod = None
        for product in RSM.products:
            if product.name == combobox.get():
                prod = product
        quan = int(quantity.get())
        RSM.restock_product(prod, quan)
    ttk.Button(restock_window, text="Confirm Order", command=confirm_restock_trans).grid(column=2, row=0)

def generate_report():
    RSM.generate_report()

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()


ttk.Button(frm, text="POS", command=conduct_pos_transaction).grid(column=0, row=1)
ttk.Button(frm, text="Inventory (Restock)", command=conduct_restock_transaction).grid(column=0, row=2)
ttk.Button(frm, text="Generate Report", command=generate_report).grid(column=0, row=3)

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
