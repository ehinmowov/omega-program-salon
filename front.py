import datetime
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import db
import sales
import crm


"""
/////////////////////////////////======== FUNCTIONS =========////////////////////////////////////////////////////////
"""


total_amount = []

"""
Clear displayed records ---------------------------------------------------------------------------------------------
"""


def r_r_treeview():
    for records in my_tree.get_children():
        values = my_tree.item(records, 'values')

        Employee_name.delete(0, END)
        Service_type.delete(0, END)
        Amount_figure.delete(0, END)

        total_amount.remove(int(values[6]))

        total = (sum(total_amount))
        entries = len(total_amount)
        Total_display.configure(text=total)
        count_display.configure(text=entries)

        my_tree.delete(records)

        save_button['state'] = 'normal'


"""
---------------------------------------------------------------------------------
"""

"""
function to refresh records ---------------------------------------------------------------------------------
"""


def refresh():
    r_r_treeview()

    global db_amount
    for rows in db.view_all():
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

        Employee_name.delete(0, END)
        Service_type.delete(0, END)
        Amount_figure.delete(0, END)

        update_button['state'] = 'disabled'
        Delete_button['state'] = 'disabled'

        get_total()


"""
 ---------------------------------------------------------------------------------
"""

"""
function to delete data from DB---------------------------------------------------------------------------------
"""


def delete():
    global total
    global values
    response = messagebox.askokcancel("Delete Data",
                                      "This will permanently delete this record, are you sure you want to continue?")
    if response == True:
        x = my_tree.selection()[0]
        # vb = my_tree.item(x, 'iid')
        # print(vb)
        values = my_tree.item(x, 'values')
        text = my_tree.item(x, 'text')

        Employee_name.delete(0, END)
        Service_type.delete(0, END)
        Amount_figure.delete(0, END)

        total_amount.remove(int(values[6]))

        total = (sum(total_amount))
        entries = len(total_amount)
        Total_display.configure(text=total)
        count_display.configure(text=entries)

        my_tree.delete(x)

        db.delete_selected(text)

        save_button['state'] = 'normal'


    else:
        Employee_name.delete(0, END)
        Service_type.delete(0, END)
        Amount_figure.delete(0, END)

        save_button['state'] = 'normal'
        update_button['state'] = 'disabled'
        Delete_button['state'] = 'disabled'


"""
 ---------------------------------------------------------------------------------
"""

"""
function to get selected row ---------------------------------------------------------------------------------
"""


def get_selected_row(event):
    data = my_tree.selection()[0]
    values = my_tree.item(data, 'values')
    Employee_name.delete(0, END)
    Service_type.delete(0, END)
    Amount_figure.delete(0, END)

    Employee_name.insert(END, values[0])
    Service_type.insert(END, values[1])
    Amount_figure.insert(END, values[6])

    save_button['state'] = 'disabled'
    update_button['state'] = 'normal'
    Delete_button['state'] = 'normal'


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
    entries = len(total_amount)
    Total_display.configure(text=total)
    count_display.configure(text=entries)


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
    if em.get() == "" or st.get() == "":
        messagebox.showerror("Empty Field",
                             "One or more fields might have been empty, please check and try again")

    else:
        try:
            db.add_entry(em.get(), st.get(), day, month, year, current_time, af.get())

            Employee_name.delete(0, END)
            Service_type.delete(0, END)
            Amount_figure.delete(0, END)

            refresh()


        except:
            messagebox.showerror("Empty Field", "Amount has to be a figure")


"""
---------------------------------------------------------------------------------
"""

"""
update function called after authentication ----------------------------------------------------------------------------
"""


def update():
    now = datetime.datetime.today()
    y = str(now)

    year = int(y[:4])
    month = int(y[5:7])
    day = int(y[8:10])
    current_time = y[11:16]


    global values
    response = messagebox.askokcancel("Update Data",
                                      "This action will update your records")
    if response:
        x = my_tree.selection()[0]
        values = my_tree.item(x, 'values')
        text = my_tree.item(x, 'text')

        db.update_selected(text, em.get(), st.get(), af.get())

        Employee_name.delete(0, END)
        Service_type.delete(0, END)
        Amount_figure.delete(0, END)

        refresh()

        save_button['state'] = 'normal'
        update_button['state'] = 'disabled'
        Delete_button['state'] = 'disabled'




"""
---------------------------------------------------------------------------------
"""

"""
Search and query DB---------------------------------------------------------------------------------
"""


def search():
    global employee
    global day
    global month
    global year

    r_r_treeview()
    if sem.get() == "" and day_input.get() == "" and month_input.get() == "" and year_input.get() == "":
        messagebox.showerror('Empty field',
                             "All fields cannot be empty")
        refresh()

    else:
        if sem.get() != "" and day_input.get() != "" and month_input.get() != "" and year_input.get() != "":

            for rows in db.search_entry_employee_byday(employee=sem.get(),
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

                search_employee_name.delete(0, END)
                day_entry.delete(0, END)
                month_entry.delete(0, END)
                year_entry.delete(0, END)

                get_total()
        else:
            pass

        if sem.get() != "" and day_input.get() == "" and month_input.get() != "" and year_input.get() != "":

            for rows in db.search_entry_employee_bymonth(employee=sem.get(),
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

                search_employee_name.delete(0, END)
                day_entry.delete(0, END)
                month_entry.delete(0, END)
                year_entry.delete(0, END)

                get_total()
        else:
            pass

        if sem.get() != "" and day_input.get() == "" and month_input.get() == "" and year_input.get() != "":

            for rows in db.search_entry_employee_byyear(employee=sem.get(),
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

                search_employee_name.delete(0, END)
                day_entry.delete(0, END)
                month_entry.delete(0, END)
                year_entry.delete(0, END)

                get_total()
        else:
            pass

        if sem.get() == "" and day_input.get() != "" and month_input.get() != "" and year_input.get() != "":

            for rows in db.search_entry_all_byday(day=day_input.get(),
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

                search_employee_name.delete(0, END)
                day_entry.delete(0, END)
                month_entry.delete(0, END)
                year_entry.delete(0, END)

                get_total()
        else:
            pass

        if sem.get() == "" and day_input.get() == "" and month_input.get() != "" and year_input.get() != "":

            for rows in db.search_entry_all_bymonth(
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

                search_employee_name.delete(0, END)
                day_entry.delete(0, END)
                month_entry.delete(0, END)
                year_entry.delete(0, END)

                get_total()
        else:
            pass

        if sem.get() == "" and day_input.get() == "" and month_input.get() == "" and year_input.get() != "":

            for rows in db.search_entry_all_byyear(year_input.get()):
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

                search_employee_name.delete(0, END)
                day_entry.delete(0, END)
                month_entry.delete(0, END)
                year_entry.delete(0, END)

                get_total()
        else:
            pass

        if sem.get() != "" and day_input.get() == "" and month_input.get() == "" and year_input.get() == "":

            for rows in db.search_entry_employee_byall(sem.get()):
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

                search_employee_name.delete(0, END)
                day_entry.delete(0, END)
                month_entry.delete(0, END)
                year_entry.delete(0, END)

                get_total()
        else:
            pass


"""
 ---------------------------------------------------------------------------------
"""

"""
/////////////////////////////////======== FUNCTIONS =========////////////////////////////////////////////////////////
"""
try:
    root = tk.Tk()

    root.title("Afrocutt")
    root.iconbitmap('afrocutt__1__FoH_icon.ico')
    root.geometry('1200x720')
    root.resizable(False, False)

    style = ttk.Style(root)
    style.theme_use("alt")

    # Label for the description of the total amount and the total itself.
    Total_label = tk.Label(root, text="Total:")
    Total_label.grid(row=0, column=0, padx=(50, 0), pady=(50, 0))
    Total_display = tk.Label(root, text='0.0000')
    Total_display.grid(row=1, column=0, padx=(50, 0))

    # Label for the count
    count_label = tk.Label(root, text="Entry:")
    count_label.grid(row=0, column=1, padx=(50, 0), pady=(50, 0))
    count_display = tk.Label(root, text='0')
    count_display.grid(row=1, column=1, padx=(50, 0))

    # Refresh Button
    crm_button = tk.Button(root, text='CRM', width=15, bg='#020202')
    crm_button.grid(row=1, column=4)

    # Switch button
    switch_button = tk.Button(root, text='Sales', width=15, command=sales.sales_window)
    switch_button.grid(row=1, column=5)

    # Tree-view
    my_tree = ttk.Treeview(root, height=15)
    my_tree['columns'] = ('employee', 'service', 'day', 'month', 'year', 'time', 'amount')
    # Columns for Tree-View
    my_tree.column("#0", width=40)
    my_tree.column("employee", anchor=W, width=240)
    my_tree.column("service", anchor=W, width=400)
    my_tree.column("day", anchor=CENTER, width=90)
    my_tree.column("month", anchor=CENTER, width=90)
    my_tree.column("year", anchor=CENTER, width=100)
    my_tree.column("time", anchor=CENTER, width=100)
    my_tree.column("amount", anchor=CENTER, width=120)
    # Naming the columns of the tree-view
    first_c = my_tree.heading("#0", text="DBN", anchor=W)
    my_tree.heading("employee", text="Employee", anchor=CENTER)
    my_tree.heading("service", text="Service", anchor=CENTER)
    my_tree.heading("day", text="Day", anchor=CENTER)
    my_tree.heading("month", text="Month", anchor=CENTER)
    my_tree.heading("year", text="Year", anchor=CENTER)
    my_tree.heading("time", text="Time", anchor=CENTER)
    my_tree.heading("amount", text="Amount", anchor=CENTER)

    my_tree.grid(row=2, column=0, rowspan=6, columnspan=8, padx=(10, 0), pady=(10, 0))

    my_tree.bind('<<TreeviewSelect>>', get_selected_row)

    # Label and entry field for the employee name
    em = tk.StringVar()
    Employee = tk.Label(root, text='Employee name:')
    Employee.grid(row=10, column=0, pady=(20, 0))
    Employee_name = tk.Entry(root, textvariable=em)
    Employee_name.grid(row=11, column=0)

    # Label and entry filed for the service type
    st = tk.StringVar()
    Service = tk.Label(root, text='Service type:')
    Service.grid(row=10, column=1, pady=(20, 0))
    Service_type = tk.Entry(root, textvariable=st)
    Service_type.grid(row=11, column=1)

    # Label and entry field for the amount paid
    af = tk.IntVar()
    Amount = tk.Label(root, text='Amount(tl):')
    Amount.grid(row=10, column=2, pady=(20, 0))
    Amount_figure = tk.Entry(root, textvariable=af)
    Amount_figure.grid(row=11, column=2)

    # Save button
    save_button = tk.Button(root, text='Save', width=10, command=saveit)
    save_button.grid(row=11, column=3)
    # Update button
    update_button = tk.Button(root, text='Update', width=10, command=update)
    update_button.grid(row=11, column=4)
    # Delete button
    Delete_button = tk.Button(root, text='Delete', width=10, command=delete)
    Delete_button.grid(row=11, column=5)

    # Filter label
    filter_label = tk.Label(root, text='Search display here...')
    filter_label.grid(row=13, column=2, pady=(40, 0))
    # input employee name for search
    sem = tk.StringVar()
    search_employee = tk.Label(root, text='Employee name:')
    search_employee.grid(row=14, column=1, pady=(20, 0))
    search_employee_name = tk.Entry(root, textvariable=sem)
    search_employee_name.grid(row=15, column=1)
    # input day
    day_input = tk.StringVar()
    day_label = tk.Label(root, text='Day:')
    day_label.grid(row=14, column=2, pady=(20, 0))
    day_entry = tk.Entry(root, textvariable=day_input, width=5)
    day_entry.grid(row=15, column=2)
    # input month
    month_input = tk.StringVar()
    month_label = tk.Label(root, text='Month:')
    month_label.grid(row=14, column=3, pady=(20, 0))
    month_entry = tk.Entry(root, textvariable=month_input, width=5)
    month_entry.grid(row=15, column=3)
    # input year
    year_input = tk.StringVar()
    year_label = tk.Label(root, text='Year:')
    year_label.grid(row=14, column=4, pady=(20, 0))
    year_entry = tk.Entry(root, textvariable=year_input, width=5)
    year_entry.grid(row=15, column=4)
    # search button
    search_button = tk.Button(root, text='Search', command=search)
    search_button.grid(row=16, column=2, pady=(20, 0))

    refresh()

    root.mainloop()

except:
    input('name: ')
