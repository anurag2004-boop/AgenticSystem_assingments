
#Here’s an example of a modular student evaluation system in Python:
#```python
def calculate_average(grades):
    return sum(grades) / len(grades)
def determine_grade(average):
    if average >= 45:
        return 'pass'
    
    else:
        return 'Fail'
def evaluate_student(name, grades):
    average = calculate_average(grades)
    grade = determine_grade(average)
    return f"{name} has an average grade of {average:.2f} and receives a grade of {grade}."
# Example usage
student_name = "Alice"
student_grades = [65, 62, 68]
result = evaluate_student(student_name, student_grades)
print(result)


