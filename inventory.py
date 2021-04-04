import datetime
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import in_db


def inventory_window():
    now = datetime.datetime.today()
    y = str(now)

    year = int(y[:4])
    month = int(y[5:7])
    day = int(y[8:10])
    current_time = y[11:16]

    window = tk.Toplevel()
    window.title('Inventory')
    window.resizable(False, False)

    style = ttk.Style(window)
    style.theme_use("alt")

    """
    Clear displayed records ---------------------------------------------------------------------------------------------
    """

    def r_r_treeview():
        for records in my_tree.get_children():
            my_tree.delete(records)

            product_entry.delete(0, END)
            pieces_entry.delete(0, END)
            sp_entry.delete(0, END)

    """
    ---------------------------------------------------------------------------------
    """

    """
    function to refresh records ---------------------------------------------------------------------------------
    """

    def refresh():
        r_r_treeview()
        for rows in in_db.view_all():
            db_id = rows[0]
            db_product = rows[1]
            db_pieces = rows[2]
            db_price = rows[3]

            my_tree.insert(parent='', index='end', iid=db_id, text=db_id,
                           values=(db_product, db_pieces, db_price))

            product_entry.delete(0, END)
            pieces_entry.delete(0, END)
            sp_entry.delete(0, END)

            update['state'] = 'disabled'
            save['state'] = 'normal'

    """
     ---------------------------------------------------------------------------------
    """

    """
    function to save/add data ---------------------------------------------------------------------------------
    """

    def saveit():
        global count
        if product_input.get() == "" or pieces_input.get() == "" or sp_input.get() == "":
            messagebox.showerror("Empty Field",
                                 "One or more fields might have been empty, please check and try again")

        else:
            in_db.add_entry(product_input.get(), pieces_input.get(), sp_input.get())

            product_entry.delete(0, END)
            pieces_entry.delete(0, END)
            sp_entry.delete(0, END)

            refresh()

    """
    ---------------------------------------------------------------------------------
    """

    """
    function to get selected row ---------------------------------------------------------------------------------
    """

    def get_selected_row(event):
        data = my_tree.selection()[0]
        values = my_tree.item(data, 'values')
        product_entry.delete(0, END)
        pieces_entry.delete(0, END)
        sp_entry.delete(0, END)

        product_entry.insert(END, values[0])
        pieces_entry.insert(END, values[1])
        sp_entry.insert(END, values[2])

        update['state'] = 'normal'
        save['state'] = 'disabled'

    """
     ---------------------------------------------------------------------------------
    """

    """
    update function called after authentication ----------------------------------------------------------------------------
    """

    def update():
        global values
        response = messagebox.askokcancel("Update Data",
                                          "This action will update your records")
        if response:
            x = my_tree.selection()[0]
            values = my_tree.item(x, 'values')
            text = my_tree.item(x, 'text')

            in_db.update_selected(text, product_input.get(), pieces_input.get(), sp_input.get())

            product_entry.delete(0, END)
            pieces_entry.delete(0, END)
            sp_entry.delete(0, END)

            refresh()

        else:
            pass

    """
    ---------------------------------------------------------------------------------
    """

    # Refresh Button
    # refresh_button = tk.Button(window, text='Refresh', width=15, bg='#020202')
    # refresh_button.grid(row=0, column=4)

    # Tree-view
    my_tree = ttk.Treeview(window, height=20)
    my_tree['columns'] = ('product', 'available pieces', 'selling price')
    # Columns for Tree-View
    my_tree.column("#0", width=40)
    my_tree.column("product", anchor=W, width=400)
    my_tree.column("available pieces", anchor=W, width=100)
    my_tree.column("selling price", anchor=CENTER, width=100)

    # Naming the columns of the tree-view
    first_c = my_tree.heading("#0", text="DBN", anchor=W)
    my_tree.heading("product", text="Product", anchor=CENTER)
    my_tree.heading("available pieces", text="Available Pieces", anchor=CENTER)
    my_tree.heading("selling price", text="Selling Price", anchor=CENTER)

    my_tree.grid(row=0, column=0, rowspan=6, columnspan=7, padx=(25, 25), pady=(30, 0))

    my_tree.bind('<<TreeviewSelect>>', get_selected_row)

    # Products dropdown

    product_input = tk.StringVar()
    product_label = Label(window, text='Product name:')
    product_label.grid(row=7, column=0, pady=(10, 0))
    product_entry = tk.Entry(window, textvariable=product_input)
    product_entry.grid(row=8, column=0, pady=(0, 10))

    pieces_input = tk.StringVar()
    pieces_label = Label(window, text='Pieces(x):', width=7)
    pieces_label.grid(row=7, column=1, pady=(10, 0))
    pieces_entry = tk.Entry(window, textvariable=pieces_input, width=5)
    pieces_entry.grid(row=8, column=1, pady=(0, 10))

    sp_input = tk.StringVar()
    sp_label = Label(window, text='Selling price:', width=8)
    sp_label.grid(row=7, column=2, pady=(10, 0))
    sp_entry = tk.Entry(window, textvariable=sp_input)
    sp_entry.grid(row=8, column=2, pady=(0, 10))

    save = tk.Button(window, text='Add Product', command=saveit)
    save.grid(row=8, column=3, pady=(10, 10))

    update = tk.Button(window, text='Update Product', command=update)
    update.grid(row=8, column=4, pady=(10, 10))

    refresh()

    window.mainloop()
