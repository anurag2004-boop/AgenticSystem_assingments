def grade_students(student_list):
    if not student_list:
        return "no students to grade"
    grades = {}
    for student in student_list:
        if student['score'] >= 90:
            grades[student] = 'A'
        elif student['score'] >= 75:
            grades[student] = 'B'
        elif student['score'] >= 60:
            grades[student] = 'C'
        else:
            grades[student] = 'F'
            return grades
        #test score of 95

        students = [
            {'name': 'alice', 'score': 92},
            {'name': 'bob', 'score': 74},
            {'name': 'carol', 'score': 61},
            {'name': 'dave', 'score': 45}
        ]
        
print(grade_students(student_list))


    
     

                        