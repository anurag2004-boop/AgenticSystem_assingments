# Storing marks of at least 8 students in a list
marks = [78, 85, 90, 88, 92, 80, 65, 70]        
# Printing the full list
print("Full list of marks:", marks)
# Printing the first 3 marks
print("First 3 marks:", marks[:3])
# Printing the last 3 marks 
print("Last 3 marks:", marks[-3:])
# Calculating and printing the highest mark
highest_mark = max(marks)
print("Highest mark:", highest_mark)
# Calculating and printing the lowest mark
lowest_mark = min(marks)
print("Lowest mark:", lowest_mark)
# Calculating and printing the average mark 
average_mark = sum(marks) / len(marks)
print("Average mark:", average_mark)
