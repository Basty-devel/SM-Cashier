import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # For styling

# Price data for products
price_data = {
    'Biscuit': 3,
    'Chicken': 5,
    'Egg': 1,
    'Fish': 3,
    'Coke': 2,
    'Bread': 2,
    'Apple': 3,
    'Onion': 3
}

buying_data = {}  # Store product and quantity

# Function to calculate discount based on membership type
def get_discount(total, membership):
    discount = 0
    if total < 25:
        return total, discount  # No discount for totals under $25
    
    if membership == "Gold":
        discount = total * 0.20  # 20% discount for Gold members
    elif membership == "Silver":
        discount = total * 0.10  # 10% discount for Silver members
    elif membership == "Bronze":
        discount = total * 0.05  # 5% discount for Bronze members
    
    return total - discount, discount  # Return the discounted total and discount applied

# Function to add product and quantity
def add_product():
    product = product_var.get()  # Get selected product
    try:
        quantity = int(quantity_entry.get())  # Get quantity as integer
        if quantity <= 0:
            messagebox.showerror("Input Error", "Quantity should be a positive number.")
            return
        
        if product in buying_data:
            buying_data[product] += quantity  # Update existing product quantity
        else:
            buying_data[product] = quantity  # Add new product and quantity
        
        update_bill()  # Update the displayed bill
        quantity_entry.delete(0, tk.END)  # Clear quantity field after entry
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid quantity.")

# Function to update bill display and apply discount
def update_bill():
    bill_text.delete('1.0', tk.END)
    
    bill_text.insert(tk.END, "SM-Cashier Copyright(C) 2024 nestler.dev\n")
    bill_text.insert(tk.END, f"{'Product':<10}{'Price':<10}{'Qty':<10}{'Subtotal':<10}\n")
    bill_text.insert(tk.END, "-" * 40 + "\n")
    
    total = 0
    
    for product, quantity in buying_data.items():
        price = price_data[product]
        subtotal = price * quantity
        total += subtotal
        bill_text.insert(tk.END, f"{product:<10}${price:<9}{quantity:<10}${subtotal:<10}\n")
    
    bill_text.insert(tk.END, "-" * 40 + "\n")

    membership_type = membership_var.get()
    discounted_total, discount_applied = get_discount(total, membership_type)

    bill_text.insert(tk.END, f"{'Subtotal':<30}${total:<10}\n")

    if discount_applied > 0:
        bill_text.insert(tk.END, f"{'Discount':<30}-${discount_applied:<10}\n")
        bill_text.insert(tk.END, f"{'Total after Discount':<30}${discounted_total:<10}\n")
    else:
        bill_text.insert(tk.END, f"{'Total (No Discount)':<30}${discounted_total:<10}\n")

    bill_text.insert(tk.END, "\nSM-Cashier Copyright(C) 2024 nestler.dev")

# Function to clear all data
def clear_all():
    buying_data.clear()  # Clear product data
    bill_text.delete('1.0', tk.END)  # Clear the bill display
    quantity_entry.delete(0, tk.END)  # Clear quantity field

# Initialize the main application window
root = tk.Tk()
root.title("Shopping Cart by www.nestler.dev")
root.geometry("650x750")
root.configure(bg='#2f2f2f')  # Set background color to dark grey

# Custom styling for buttons with rounded corners
style = ttk.Style()
style.configure("TButton", 
                background='#ADD8E6',  # Light blue
                foreground='white', 
                font=("Helvetica", 12), 
                borderwidth=0)
style.map("TButton", background=[('active', '#87CEEB')])  # Change color on hover (lighter blue)

# Title label
title_label = tk.Label(root, text="Product Entry", font=("Helvetica", 16, "bold"), bg='#2f2f2f', fg='#ffffff')
title_label.pack(pady=10)

# Dropdown for product selection
product_var = tk.StringVar(root)
product_var.set("Select Product")
product_menu = tk.OptionMenu(root, product_var, *price_data.keys())
product_menu.config(bg='#ffffff', fg='#333333', font=("Helvetica", 12))
product_menu.pack(pady=10)

# Quantity input field
quantity_label = tk.Label(root, text="Quantity", font=("Helvetica", 12), bg='#2f2f2f', fg='#ffffff')
quantity_label.pack()
quantity_entry = tk.Entry(root, font=("Helvetica", 12))
quantity_entry.pack(pady=5)

# Membership Dropdown for selecting membership type
membership_var = tk.StringVar(root)
membership_var.set("None")
membership_label = tk.Label(root, text="Membership", font=("Helvetica", 12), bg='#2f2f2f', fg='#ffffff')
membership_label.pack(pady=10)
membership_menu = tk.OptionMenu(root, membership_var, "None", "Gold", "Silver", "Bronze")
membership_menu.config(bg='#ffffff', fg='#333333', font=("Helvetica", 12))
membership_menu.pack(pady=10)

# Add Product button with custom style
add_button = ttk.Button(root, text="Add Product", command=add_product, style="TButton")
add_button.pack(pady=10)

# Bill display area
bill_text = tk.Text(root, height=15, width=40, font=("Courier", 10), bg='#ffffff', fg='#000000')
bill_text.pack(pady=10)

# Clear all button with custom style
clear_button = ttk.Button(root, text="Clear All", command=clear_all, style="TButton")
clear_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
