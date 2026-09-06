MENU = [
    {"item": "chicken_biryani", "price": 250, "available_quantity": 5},
    {"item": "paneer_tikka", "price": 180, "available_quantity": 0},
    {"item": "veg_fried_rice", "price": 150, "available_quantity": 8},
    {"item": "butter_naan", "price": 40, "available_quantity": 20},
    {"item": "gulab_jamun", "price": 60, "available_quantity": 3},
]

def get_menu():
    """
    Retrieve the list of menu items that are currently in stock.
    Returns only the items with an available quantity greater than zero.
    """
    return [item for item in MENU if item["available_quantity"] > 0]

def place_order(item, quantity):
    """
    Place an order for a specific menu item.
    Validates if the item exists and has sufficient available quantity.
    Returns order confirmation details on success, or an error message string on failure.
    """
    for menu_item in MENU:
        if menu_item["item"] == item:
            if menu_item["available_quantity"] >= quantity:
                # On success, decrement available_quantity
                menu_item["available_quantity"] -= quantity
                total_price = menu_item["price"] * quantity
                
                # Return confirmation
                return {
                    "item": item,
                    "quantity_ordered": quantity,
                    "total_price": total_price
                }
            else:
                # Failure: Insufficient quantity
                return f"Error: Insufficient quantity for '{item}'. Only {menu_item['available_quantity']} available."
    
    # Failure: Item not found
    return f"Error: Item '{item}' not found on the menu."

if __name__ == "__main__":
    print(get_menu())
    print(place_order("chicken_biryani", 2))
    print(place_order("paneer_tikka", 1))
    print(place_order("veg_fried_rice", 3))
    print(place_order("butter_naan", 5))
    