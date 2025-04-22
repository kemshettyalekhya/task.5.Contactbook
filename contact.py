import tkinter as tk
from tkinter import messagebox, ttk

# Global list to store contact dictionaries
contacts = []

# Function to update the contact listbox
def refresh_contacts():
    contact_list.delete(*contact_list.get_children())
    for i, contact in enumerate(contacts):
        contact_list.insert("", "end", iid=i, values=(contact['name'], contact['phone']))

# Add contact
def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if not name or not phone:
        messagebox.showwarning("Missing Info", "Name and Phone are required.")
        return

    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    refresh_contacts()
    clear_fields()

# Delete contact
def delete_contact():
    selected = contact_list.selection()
    if not selected:
        messagebox.showwarning("Select Contact", "Please select a contact to delete.")
        return
    index = int(selected[0])
    contacts.pop(index)
    refresh_contacts()
    clear_fields()

# Update contact
def update_contact():
    selected = contact_list.selection()
    if not selected:
        messagebox.showwarning("Select Contact", "Please select a contact to update.")
        return
    index = int(selected[0])
    contacts[index] = {
        'name': name_entry.get().strip(),
        'phone': phone_entry.get().strip(),
        'email': email_entry.get().strip(),
        'address': address_entry.get().strip()
    }
    refresh_contacts()
    clear_fields()

# Fill form on selection
def on_select(event):
    selected = contact_list.selection()
    if not selected:
        return
    index = int(selected[0])
    contact = contacts[index]
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

    name_entry.insert(0, contact['name'])
    phone_entry.insert(0, contact['phone'])
    email_entry.insert(0, contact['email'])
    address_entry.insert(0, contact['address'])

# Clear input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Search contacts
def search_contact():
    query = search_entry.get().lower()
    contact_list.delete(*contact_list.get_children())
    for i, contact in enumerate(contacts):
        if query in contact['name'].lower() or query in contact['phone']:
            contact_list.insert("", "end", iid=i, values=(contact['name'], contact['phone']))

# GUI setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("700x500")
root.configure(bg="#f7f9fc")

title = tk.Label(root, text="Contact Book", font=("Helvetica", 20, "bold"), bg="#34495e", fg="white", pady=10)
title.pack(fill=tk.X)

# Entry Frame
entry_frame = tk.Frame(root, bg="#ecf0f1", bd=2, relief="groove", padx=10, pady=10)
entry_frame.place(x=20, y=60, width=300, height=300)

tk.Label(entry_frame, text="Name:", font=("Arial", 12), bg="#ecf0f1").pack(anchor="w")
name_entry = tk.Entry(entry_frame, font=("Arial", 12))
name_entry.pack(fill=tk.X, pady=5)

tk.Label(entry_frame, text="Phone:", font=("Arial", 12), bg="#ecf0f1").pack(anchor="w")
phone_entry = tk.Entry(entry_frame, font=("Arial", 12))
phone_entry.pack(fill=tk.X, pady=5)

tk.Label(entry_frame, text="Email:", font=("Arial", 12), bg="#ecf0f1").pack(anchor="w")
email_entry = tk.Entry(entry_frame, font=("Arial", 12))
email_entry.pack(fill=tk.X, pady=5)

tk.Label(entry_frame, text="Address:", font=("Arial", 12), bg="#ecf0f1").pack(anchor="w")
address_entry = tk.Entry(entry_frame, font=("Arial", 12))
address_entry.pack(fill=tk.X, pady=5)

# Buttons
btn_frame = tk.Frame(entry_frame, bg="#ecf0f1")
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Add", font=("Arial", 10), bg="#2ecc71", fg="white", command=add_contact, width=8).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update", font=("Arial", 10), bg="#3498db", fg="white", command=update_contact, width=8).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", font=("Arial", 10), bg="#e74c3c", fg="white", command=delete_contact, width=8).grid(row=0, column=2, padx=5)

# Search box
search_frame = tk.Frame(root, bg="#f7f9fc")
search_frame.place(x=340, y=60, width=330, height=40)
search_entry = tk.Entry(search_frame, font=("Arial", 12))
search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
tk.Button(search_frame, text="Search", font=("Arial", 10), command=search_contact, bg="#8e44ad", fg="white").pack(side=tk.LEFT, padx=5)

# Contact list
list_frame = tk.Frame(root, bg="#f7f9fc")
list_frame.place(x=340, y=110, width=330, height=250)

columns = ("name", "phone")
contact_list = ttk.Treeview(list_frame, columns=columns, show="headings", height=10)
contact_list.heading("name", text="Name")
contact_list.heading("phone", text="Phone")
contact_list.column("name", width=160)
contact_list.column("phone", width=150)
contact_list.pack(fill=tk.BOTH, expand=True)
contact_list.bind("<<TreeviewSelect>>", on_select)

# Reset Button
tk.Button(root, text="Clear Fields", font=("Arial", 10), command=clear_fields, bg="#95a5a6", fg="white").place(x=120, y=370)

root.mainloop()
