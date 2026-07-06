1. Function to display student info
def display_student(student_id, name):
    print("\nStudent Details")
    print(f"Student ID: {student_id}")
    print(f"Student Name: {name}")

2. Function to calculate and display total
def calculate_total(mark1, mark2, mark3, mark4, mark5):
    total = mark1 + mark2 + mark3 + mark4 + mark5
    print(f"\nTotal Marks: {total}")

3. Function to calculate and display percentage
def calculate_percentage(mark1, mark2, mark3, mark4, mark5):
    total = mark1 + mark2 + mark3 + mark4 + mark5
    percentage = total / 5  # out of 100
    print(f"\nPercentage: {percentage}%")

4. Function to display grade
def find_grade(percentage):
    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "Fail"
    print(f"\nGrade: {grade}")

5. Function to display highest mark
def highest_mark(mark1, mark2, mark3, mark4, mark5):
    marks = [mark1, mark2, mark3, mark4, mark5]
    print(f"\nHighest Mark: {max(marks)}")

6. Function to display lowest mark
def lowest_mark(mark1, mark2, mark3, mark4, mark5):
    marks = [mark1, mark2, mark3, mark4, mark5]
    print(f"\nLowest Mark: {min(marks)}")

7. Function to display Pass/Fail
def pass_fail(mark1, mark2, mark3, mark4, mark5):
    marks = [mark1, mark2, mark3, mark4, mark5]
    for m in marks:
        if m < 35:
            print("\nResult: Fail")
            return
    print("\nResult: Pass")

Main Program:
student_id = int(input("Enter Student ID: "))
student_name = input("Enter Student Name: ")

m1 = int(input("Enter maths Marks: "))
m2 = int(input("Enter english Marks: "))
m3 = int(input("Enter telugu Marks: "))
m4 = int(input("Enter social Marks: "))
m5 = int(input("Enter hindi Marks: "))

display_student(student_id, student_name)
calculate_total(m1, m2, m3, m4, m5)
calculate_percentage(m1, m2, m3, m4, m5)

total = m1 + m2 + m3 + m4 + m5
perc = total / 5
find_grade(perc)
highest_mark(m1, m2, m3, m4, m5)
lowest_mark(m1, m2, m3, m4, m5)
pass_fail(m1, m2, m3, m4, m5)