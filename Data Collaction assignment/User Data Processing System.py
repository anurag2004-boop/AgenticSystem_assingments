from Dictionary import contact_book
from tuple import my_tuple 
from Sets import my_set
# Function to display contact book
def display_contact_book():
    print("Contact Book:")
    for name, phone in contact_book.items():
        print(f"{name}: {phone}")   
# Function to display tuple elements
def display_tuple_elements():
    print("Tuple Elements:")
    for element in my_tuple:
        print(element)
# Function to display set elements
def display_set_elements():
    print("Set Elements:")
    for element in my_set:
        print(element)  
# Main function to run the program
def main():
    display_contact_book()
    print("\n")
    display_tuple_elements()
    print("\n")
    display_set_elements()

if __name__ == "__main__":
    main()
