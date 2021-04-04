import datetime
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import inventory
import in_db
import sales_db
from getpass import getpass
from PIL import ImageTk, Image



def sales_window():
    global window
    global product
    product = []
    total_amount = []
    now = datetime.datetime.today()
    y = str(now)

    year = int(y[:4])
    month = int(y[5:7])
    day = int(y[8:10])
    current_time = y[11:16]

    window = tk.Toplevel()
    window.title('Sales')
    window.geometry('800x700')
    window.resizable(False, False)

    style = ttk.Style(window)
    style.theme_use("alt")

    """
    Clear displayed records ---------------------------------------------------------------------------------------------
    """

    def r_r_treeview():
        for records in my_tree.get_children():
            values = my_tree.item(records, 'values')

            product_drop.delete(0, END)
            pieces_entry.delete(0, END)
            price_label.configure(text='0')

            total_amount.remove(int(values[6]))

            total = (sum(total_amount))
            total_sales_label.configure(text=total)

            my_tree.delete(records)

    """
    ---------------------------------------------------------------------------------
    """

    """
    function to refresh records ---------------------------------------------------------------------------------
    """

    def refresh():
        r_r_treeview()

        global db_amount
        for rows in sales_db.view_all():
            db_id = rows[0]
            db_product = rows[1]
            db_pieces = rows[2]
            db_day = rows[3]
            db_month = rows[4]
            db_year = rows[5]
            db_time = rows[6]
            db_amount = rows[7]

            my_tree.insert(parent='', index='end', iid=db_id, text=db_id,
                           values=(db_product, db_pieces, db_day, db_month, db_year, db_time, db_amount))

            product_drop.delete(0, END)
            pieces_entry.delete(0, END)
            price_label.configure(text='0')

            save['state'] = 'disabled'

            get_total()

    """
     ---------------------------------------------------------------------------------
    """

    """
    function to save/add data ---------------------------------------------------------------------------------
    """

    def saveit():
        now = datetime.datetime.today()
        y = str(now)

        year = int(y[:4])
        month = int(y[5:7])
        day = int(y[8:10])
        current_time = y[11:16]
        global count

        sales_db.add_entry(selected_product.get(), pieces_input.get(), day, month, year, current_time, total_price)
        update_inventory()

        product_drop.delete(0, END)
        pieces_entry.delete(0, END)
        price_label.configure(text='0')

        #  update_inventory()

        refresh()

    """
    ---------------------------------------------------------------------------------
    """

    """
    function to calculate and update Total ---------------------------------------------------------------------------------
    """

    def get_total():
        global amount

        for records in my_tree.get_children():
            values = my_tree.item(records, 'values')
            amount = int(values[6])

        total_amount.append(amount)

        total = (sum(total_amount))
        total_sales_label.configure(text=total)

    """
    ---------------------------------------------------------------------------------
    """

    """
    Search and query DB---------------------------------------------------------------------------------
    """

    def search():
        global product_s_drop
        global day
        global month
        global year

        r_r_treeview()
        if selected_product_s.get() == "" and day_input.get() == "" and month_input.get() == "" and year_input.get() == "":
            messagebox.showerror('Empty field',
                                 "All fields cannot be empty")
            refresh()

        else:
            if selected_product_s.get() != "" and day_input.get() != "" and month_input.get() != "" and year_input.get() != "":

                for rows in sales_db.search_entry_product_byday(product=selected_product_s.get(),
                                                                day=day_input.get(),
                                                                month=month_input.get(),
                                                                year=year_input.get()):
                    db_id = rows[0]
                    db_employee = rows[1]
                    db_service = rows[2]
                    db_day = rows[3]
                    db_month = rows[4]
                    db_year = rows[5]
                    db_time = rows[6]
                    db_amount = rows[7]

                    my_tree.insert(parent='', index='end', iid=db_id, text=db_id,
                                   values=(db_employee, db_service, db_day, db_month, db_year, db_time, db_amount))

                    product_s_drop.delete(0, END)
                    day_entry.delete(0, END)
                    month_entry.delete(0, END)
                    year_entry.delete(0, END)

                    get_total()
            else:
                pass

            if selected_product_s.get() != "" and day_input.get() == "" and month_input.get() != "" and year_input.get() != "":

                for rows in sales_db.search_entry_product_bymonth(product=selected_product_s.get(),
                                                                  month=month_input.get(),
                                                                  year=year_input.get()):
                    db_id = rows[0]
                    db_employee = rows[1]
                    db_service = rows[2]
                    db_day = rows[3]
                    db_month = rows[4]
                    db_year = rows[5]
                    db_time = rows[6]
                    db_amount = rows[7]

                    my_tree.insert(parent='', index='end', iid=db_id, text=db_id,
                                   values=(db_employee, db_service, db_day, db_month, db_year, db_time, db_amount))

                    product_s_drop.delete(0, END)
                    day_entry.delete(0, END)
                    month_entry.delete(0, END)
                    year_entry.delete(0, END)

                    get_total()
            else:
                pass

            if selected_product_s.get() != "" and day_input.get() == "" and month_input.get() == "" and year_input.get() != "":

                for rows in sales_db.search_entry_product_byyear(product=selected_product_s.get(),
                                                                 year=year_input.get()):
                    db_id = rows[0]
                    db_employee = rows[1]
                    db_service = rows[2]
                    db_day = rows[3]
                    db_month = rows[4]
                    db_year = rows[5]
                    db_time = rows[6]
                    db_amount = rows[7]

                    my_tree.insert(parent='', index='end', iid=db_id, text=db_id,
                                   values=(db_employee, db_service, db_day, db_month, db_year, db_time, db_amount))

                    product_s_drop.delete(0, END)
                    day_entry.delete(0, END)
                    month_entry.delete(0, END)
                    year_entry.delete(0, END)

                    get_total()
            else:
                pass

            if selected_product_s.get() == "" and day_input.get() != "" and month_input.get() != "" and year_input.get() != "":

                for rows in sales_db.search_entry_all_byday(day=day_input.get(),
                                                            month=month_input.get(),
                                                            year=year_input.get()):
                    db_id = rows[0]
                    db_employee = rows[1]
                    db_service = rows[2]
                    db_day = rows[3]
                    db_month = rows[4]
                    db_year = rows[5]
                    db_time = rows[6]
                    db_amount = rows[7]

                    my_tree.insert(parent='', index='end', iid=db_id, text=db_id,
                                   values=(db_employee, db_service, db_day, db_month, db_year, db_time, db_amount))

                    product_s_drop.delete(0, END)
                    day_entry.delete(0, END)
                    month_entry.delete(0, END)
                    year_entry.delete(0, END)

                    get_total()
            else:
                pass

            if selected_product_s.get() == "" and day_input.get() == "" and month_input.get() != "" and year_input.get() != "":

                for rows in sales_db.search_entry_all_bymonth(
                        month=month_input.get(),
                        year=year_input.get()):
                    db_id = rows[0]
                    db_employee = rows[1]
                    db_service = rows[2]
                    db_day = rows[3]
                    db_month = rows[4]
                    db_year = rows[5]
                    db_time = rows[6]
                    db_amount = rows[7]

                    my_tree.insert(parent='', index='end', iid=db_id, text=db_id,
                                   values=(db_employee, db_service, db_day, db_month, db_year, db_time, db_amount))

                    product_s_drop.delete(0, END)
                    day_entry.delete(0, END)
                    month_entry.delete(0, END)
                    year_entry.delete(0, END)

                    get_total()
            else:
                pass

            if selected_product_s.get() == "" and day_input.get() == "" and month_input.get() == "" and year_input.get() != "":

                for rows in sales_db.search_entry_all_byyear(year_input.get()):
                    db_id = rows[0]
                    db_employee = rows[1]
                    db_service = rows[2]
                    db_day = rows[3]
                    db_month = rows[4]
                    db_year = rows[5]
                    db_time = rows[6]
                    db_amount = rows[7]

                    my_tree.insert(parent='', index='end', iid=db_id, text=db_id,
                                   values=(db_employee, db_service, db_day, db_month, db_year, db_time, db_amount))

                    product_s_drop.delete(0, END)
                    day_entry.delete(0, END)
                    month_entry.delete(0, END)
                    year_entry.delete(0, END)

                    get_total()
            else:
                pass

            if selected_product_s.get() != "" and day_input.get() == "" and month_input.get() == "" and year_input.get() == "":

                for rows in sales_db.search_entry_product_byall(selected_product_s.get()):
                    db_id = rows[0]
                    db_employee = rows[1]
                    db_service = rows[2]
                    db_day = rows[3]
                    db_month = rows[4]
                    db_year = rows[5]
                    db_time = rows[6]
                    db_amount = rows[7]

                    my_tree.insert(parent='', index='end', iid=db_id, text=db_id,
                                   values=(db_employee, db_service, db_day, db_month, db_year, db_time, db_amount))

                    product_s_drop.delete(0, END)
                    day_entry.delete(0, END)
                    month_entry.delete(0, END)
                    year_entry.delete(0, END)

                    get_total()
            else:
                pass

    """
     ---------------------------------------------------------------------------------
    """

    # Refresh Button
    # refresh_button = tk.Button(window, text='Refresh', width=15, bg='#020202')
    # refresh_button.grid(row=0, column=4)

    sales_label = Label(window, text='Sales:')
    sales_label.grid(row=0, column=0, pady=(10, 0))
    total_sales_label = Label(window, text='0.00')
    total_sales_label.grid(row=1, column=0, pady=(10, 0))

    # Tree-view
    my_tree = ttk.Treeview(window, height=15)
    my_tree['columns'] = ('product', 'pieces', 'day', 'month', 'year', 'time', 'amount')
    # Columns for Tree-View
    my_tree.column("#0", width=40)
    my_tree.column("product", anchor=W, width=400)
    my_tree.column("pieces", anchor=W, width=50)
    my_tree.column("day", anchor=CENTER, width=50)
    my_tree.column("month", anchor=CENTER, width=50)
    my_tree.column("year", anchor=CENTER, width=50)
    my_tree.column("time", anchor=CENTER, width=50)
    my_tree.column("amount", anchor=CENTER, width=50)
    # Naming the columns of the tree-view
    first_c = my_tree.heading("#0", text="DBN", anchor=W)
    my_tree.heading("product", text="Product", anchor=CENTER)
    my_tree.heading("pieces", text="Pieces", anchor=CENTER)
    my_tree.heading("day", text="Day", anchor=CENTER)
    my_tree.heading("month", text="Month", anchor=CENTER)
    my_tree.heading("year", text="Year", anchor=CENTER)
    my_tree.heading("time", text="Time", anchor=CENTER)
    my_tree.heading("amount", text="Amount", anchor=CENTER)

    my_tree.grid(row=2, column=0, rowspan=6, columnspan=7, padx=(25, 0), pady=(30, 0))

    Inventory = tk.Button(window, text='Inventory', command=inventory.inventory_window)
    Inventory.grid(row=1, column=4, pady=(10, 0))

    products_label = Label(window, text='Product:')
    products_label.grid(row=9, column=0, pady=(10, 0))

    # Products dropdown
    def get_product_price():
        global total_price

        if selected_product.get() == "" or pieces_input.get() == "":
            messagebox.showerror("Empty Field",
                                 "One or more fields might have been empty, please check and try again")

        else:
            try:
                for rows in in_db.search_entry(selected_product.get()):
                    price = int(rows[3])
                    total_price = int(pieces_input.get()) * price
                    price_label.configure(text=total_price)

                    save['state'] = 'normal'


            except:
                messagebox.showerror("Empty Field", "pieces has to be a figure")

    def update_inventory():
        global text_id, product_name, new_pieces, price_p
        for rows in in_db.search_entry(selected_product.get()):
            text_id = rows[0]
            product_name = rows[1]
            price_p = rows[3]
            pieces = int(rows[2])
            new_pieces = pieces - int(pieces_input.get())

        in_db.update_selected(text_id, product_name, new_pieces, price_p)

    def get_products():
        global pieces_input
        global product_s_drop
        global selected_product_s
        global selected_product
        global product_drop
        global pieces_entry
        for rows in in_db.view_all():
            product.append(rows[1])
            item = rows[1]
            price = rows[3]
            print(f'{item} is {price}tl')

        products = product
        products.sort()

        selected_product = tk.StringVar()

        product_drop = ttk.Combobox(window, textvariable=selected_product)
        product_drop['values'] = products
        product_drop['state'] = 'readonly'
        product_drop.grid(row=10, column=0, pady=(10, 0))

        products_s = product
        products_s.sort()

        selected_product_s = tk.StringVar()

        product_s_drop = ttk.Combobox(window, textvariable=selected_product_s)
        product_s_drop['values'] = products_s
        product_s_drop['state'] = 'readonly'
        product_s_drop.grid(row=13, column=0, pady=(10, 0))

        def handle_selection_s(event):
            print('today is', selected_product_s.get())
            print(product_s_drop.current())

        product_s_drop.bind('<<ComboboxSelected>>', handle_selection_s)

        productS_label = Label(window, text='Product:')
        productS_label.grid(row=12, column=0, pady=(10, 0))

    pieces_input = tk.StringVar()
    pieces_label = Label(window, text='Pieces(x):')
    pieces_label.grid(row=9, column=1, pady=(10, 0))
    pieces_entry = tk.Entry(window, textvariable=pieces_input, width=5)
    pieces_entry.grid(row=10, column=1)

    goB = tk.Button(window, text='Get total', width=8, command=get_product_price)
    goB.grid(row=10, column=2, pady=(10, 0))

    total_label = Label(window, text='Total:')
    total_label.grid(row=9, column=3, pady=(10, 0))
    price_label = Label(window, text='0.00')
    price_label.grid(row=10, column=3, pady=(10, 0))

    save = tk.Button(window, text='Save', width=8, command=saveit)
    save.grid(row=10, column=4, pady=(10, 0))

    filter_label = tk.Label(window, text='Search display here...')
    filter_label.grid(row=11, column=1, pady=(40, 0))

    # input employee name for search

    # input day
    day_input = tk.StringVar()
    day_label = tk.Label(window, text='Day:')
    day_label.grid(row=12, column=1, pady=(20, 0))
    day_entry = tk.Entry(window, textvariable=day_input, width=5)
    day_entry.grid(row=13, column=1)
    # input month
    month_input = tk.StringVar()
    month_label = tk.Label(window, text='Month:')
    month_label.grid(row=12, column=2, pady=(20, 0))
    month_entry = tk.Entry(window, textvariable=month_input, width=5)
    month_entry.grid(row=13, column=2)
    # input year
    year_input = tk.StringVar()
    year_label = tk.Label(window, text='Year:')
    year_label.grid(row=12, column=3, pady=(20, 0))
    year_entry = tk.Entry(window, textvariable=year_input, width=5)
    year_entry.grid(row=13, column=3)
    # search button
    search_button = tk.Button(window, text='Search', command=search)
    search_button.grid(row=14, column=1, pady=(20, 0))

    get_products()

    refresh()

    window.mainloop()
