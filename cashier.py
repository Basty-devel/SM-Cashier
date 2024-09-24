#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cashier.py
#  
#  Copyright 2024  <snestler@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import tkinter as tk
from tkinter import messagebox

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
    """
    Applies a discount based on membership level if total is >= $25.
    - Gold: 20% discount
    - Silver: 10% discount
    - Bronze: 5% discount
    - None: No discount
    """
    discount = 0
    if total < 25:
        return total, discount  # No discount for totals under $25
    
    # Apply discount based on membership
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
    bill_text.delete('1.0', tk.END)  # Clear the bill text area
    total = 0
    bill_text.insert(tk.END, f"{'Product':<10}{'Price':<10}{'Qty':<10}{'Subtotal':<10}\n")
    bill_text.insert(tk.END, "-" * 40 + "\n")
    
    for product, quantity in buying_data.items():
        price = price_data[product]
        subtotal = price * quantity
        total += subtotal
        bill_text.insert(tk.END, f"{product:<10}${price:<9}{quantity:<10}${subtotal:<10}\n")
    
    bill_text.insert(tk.END, "-" * 40 + "\n")

    # Get the membership type and apply discount
    membership_type = membership_var.get()
    discounted_total, discount_applied = get_discount(total, membership_type)

    # Display total with and without discount
    bill_text.insert(tk.END, f"{'Subtotal':<30}${total:<10}\n")

    # If a discount is applied, show it in the bill
    if discount_applied > 0:
        bill_text.insert(tk.END, f"{'Discount':<30}-${discount_applied:<10}\n")
        bill_text.insert(tk.END, f"{'Total after Discount':<30}${discounted_total:<10}")
    else:
        bill_text.insert(tk.END, f"{'Total (No Discount)':<30}${discounted_total:<10}")

# Function to clear all data
def clear_all():
    buying_data.clear()  # Clear product data
    bill_text.delete('1.0', tk.END)  # Clear the bill display
    quantity_entry.delete(0, tk.END)  # Clear quantity field

# Initialize the main application window
root = tk.Tk()
root.title("Shopping Cart with Discount")
root.geometry("400x550")
root.configure(bg='#f0f4f7')  # Set background color

# Title label
title_label = tk.Label(root, text="Product Entry", font=("Helvetica", 16, "bold"), bg='#f0f4f7', fg='#333333')
title_label.pack(pady=10)

# Dropdown for product selection
product_var = tk.StringVar(root)
product_var.set("Select Product")  # Default option
product_menu = tk.OptionMenu(root, product_var, *price_data.keys())
product_menu.config(bg='#ffffff', fg='#333333', font=("Helvetica", 12))
product_menu.pack(pady=10)

# Quantity input field
quantity_label = tk.Label(root, text="Quantity", font=("Helvetica", 12), bg='#f0f4f7', fg='#333333')
quantity_label.pack()
quantity_entry = tk.Entry(root, font=("Helvetica", 12))
quantity_entry.pack(pady=5)

# Membership Dropdown for selecting membership type
membership_var = tk.StringVar(root)
membership_var.set("None")  # Default membership
membership_label = tk.Label(root, text="Membership", font=("Helvetica", 12), bg='#f0f4f7', fg='#333333')
membership_label.pack(pady=10)
membership_menu = tk.OptionMenu(root, membership_var, "None", "Gold", "Silver", "Bronze")
membership_menu.config(bg='#ffffff', fg='#333333', font=("Helvetica", 12))
membership_menu.pack(pady=10)

# Add Product button
add_button = tk.Button(root, text="Add Product", command=add_product, bg='#4CAF50', fg='white', font=("Helvetica", 12), width=15)
add_button.pack(pady=10)

# Bill display area
bill_text = tk.Text(root, height=15, width=40, font=("Courier", 10))
bill_text.pack(pady=10)

# Clear all button
clear_button = tk.Button(root, text="Clear All", command=clear_all, bg='#FF5722', fg='white', font=("Helvetica", 12), width=15)
clear_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
