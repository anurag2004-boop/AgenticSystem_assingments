
  
my_tuple = (1, "Hello", 3.14, True)
# Accessing elements of a tuple
print("First element:", my_tuple[0])  # Output: 1
print("Second element:", my_tuple[1])  # Output: Hello
print("Last element:", my_tuple[-1])   # Output: True
# Sets are unordered collections of unique items. They are defined using curly braces {} and can contain elements of different data types. Sets do not allow duplicate values.
# Example of a set
my_set = {1, 2, 3, 4, 5}
# Adding an element to a set
my_set.add(6)
print("Set after adding an element:", my_set)  # Output: {1, 2, 3, 4, 5, 6}
# Removing an element from a set
my_set.remove(3)
print("Set after removing an element:", my_set)  # Output: {1, 2, 4, 5, 6}
# Checking if an element is in a set
print("Is 4 in the set?", 4 in my_set)  # Output: True
print("Is 3 in the set?", 3 in my_set)  # Output: False
# Performing set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
# Union of sets
union_set = set_a.union(set_b)
print("Union of set_a and set_b:", union_set)  # Output: {1, 2, 3, 4, 5}
# Intersection of sets
intersection_set = set_a.intersection(set_b)
print("Intersection of set_a and set_b:", intersection_set)  # Output: {3}
# Difference of sets    
difference_set = set_a.difference(set_b)
print("Difference of set_a and set_b:", difference_set)  # Output: {1, 2}
# Symmetric difference of sets
sym_diff_set = set_a.symmetric_difference(set_b)

print("Symmetric difference of set_a and set_b:", sym_diff_set)  # Output: {1, 2, 4, 5}


