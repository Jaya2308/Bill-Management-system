import tkinter as tk
from tkinter import ttk

class BillManagementSystem:
    def __init__(self, master):
        self.master = master
        master.title("Bill Management System")

        # Configure the root window to be resizable
        master.rowconfigure(0, weight=1)
        master.columnconfigure(0, weight=1)

        # Create labels and entry fields for bill details
        self.label_bill_no = ttk.Label(master, text="Bill No:")
        self.label_bill_no.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.entry_bill_no = ttk.Entry(master)
        self.entry_bill_no.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.label_bill_date = ttk.Label(master, text="Bill Date:")
        self.label_bill_date.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_bill_date = ttk.Entry(master)
        self.entry_bill_date.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        self.label_customer_name = ttk.Label(master, text="Customer Name:")
        self.label_customer_name.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.entry_customer_name = ttk.Entry(master)
        self.entry_customer_name.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        self.label_amount = ttk.Label(master, text="Amount:")
        self.label_amount.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.entry_amount = ttk.Entry(master)
        self.entry_amount.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        # Create a button to save the bill
        self.button_save = ttk.Button(master, text="Save Bill", command=self.save_bill)
        self.button_save.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        # Configure the row and column weights for auto-adjustment
        for i in range(5):
            master.rowconfigure(i, weight=1)
        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)

    def save_bill(self):
        # Get the values from the entry fields
        bill_no = self.entry_bill_no.get()
        bill_date = self.entry_bill_date.get()
        customer_name = self.entry_customer_name.get()
        amount = self.entry_amount.get()

        # Print the bill details (you can save them to a file or database)
        print("Bill No:", bill_no)
        print("Bill Date:", bill_date)
        print("Customer Name:", customer_name)
        print("Amount:", amount)

        # Clear the entry fields
        self.entry_bill_no.delete(0, tk.END)
        self.entry_bill_date.delete(0, tk.END)
        self.entry_customer_name.delete(0, tk.END)
        self.entry_amount.delete(0, tk.END)

root = tk.Tk()
app = BillManagementSystem(root)
root.mainloop()
