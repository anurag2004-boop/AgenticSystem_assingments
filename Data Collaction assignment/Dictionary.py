# Creating a contact book using a dictionary
contact_book = {
    "Ravi": "123-456-7890",
    "Bob": "234-567-8901",
    "Charlie": "345-678-9012"
}   
# Adding a new contact
contact_book["Alice"] = "456-789-0123"  
# Updating an existing contactcontact_book["Ravi"] = "987-654-3210"  
# Deleting a contactdel contact_book["Bob"]  
# Accessing a contact's phone numberprint(contact_book["Charlie"])  
# Printing the entire contact bookprint(contact_book)
# Iterating through the contact book and printing each contact's name and phone number
for name, phone in contact_book.items():
    print(f"{name}: {phone}")   
# Checking if a contact exists in the contact book
if "Alice" in contact_book:
    print("Alice's phone number is:", contact_book["Alice"])
# Getting a list of all contact names
contact_names = list(contact_book.keys())
print("Contact names:", contact_names)
# Getting a list of all phone numbers
contact_numbers = list(contact_book.values())
print("Contact numbers:", contact_numbers)
# Getting a list of all contact name and phone number pairs
contact_items = list(contact_book.items())
print("Contact items:", contact_items)

