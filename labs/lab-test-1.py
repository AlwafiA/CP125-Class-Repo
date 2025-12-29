asking_input = int(input("Enter the student's mark: "))

def determine_mark(mark):
        return mark



def determine_grade(mark):
    if (mark >= 80) and (mark <=100):
            grade ="A"
    elif mark >= 60:
            grade ="B"
    elif mark >= 50:
            grade ="C"
    elif mark >= 40:
            grade ="D"
    else : 
            grade ="F"
    if mark < 0 or mark > 100:
            print("Invalid mark entered. Please enter a mark between 0 and 100.")
            return None
    print(f"Mark: {mark}.0 , Grade:{grade}")

output = determine_grade(asking_input)


#def output(marking , grading):
    #print(f"Mark: {mark}.0")
    #print(f"Grade: {grade}")

    
#PROBLEM STATEMENT 
"""
Write a Python program that checks the grade for one student.
1. Define a function called determine_grade that accepts a mark and returns a
grade:
○ 80 or more → "A"
○ 60 to 79 → "B"
○ 50 to 59 → "C"
○ 40 to 49 → "D"
○ Less than 40 → "F"
2. In the main part of the program:
○ Ask the user to enter the students mark.
○ Use the determine_grade function to get the grade.
○ Print the students mark and grade.
Expected output:
Enter the student's mark: 72
Mark: 72.0, Grade: B
"""