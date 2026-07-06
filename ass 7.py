def process_student_results(student_id, student_name, subject_marks, attendance_percentage, assignment_score, extracurricular_points):
1. Calculate total marks:
    total_marks = sum(subject_marks.values())
    
2. Calculate average marks:
    num_subjects = len(subject_marks)
    average = total_marks / num_subjects
    
3. Add 10% assignment contribution:
    assignment_contribution = assignment_score * 0.10
    average += assignment_contribution
    
4. Add extracurricular points:
    average += extracurricular_points
    
5. Attendance check: reduce 5 marks if <75%:
    attendance_status = "Good Attendance"
    if attendance_percentage < 75:
        average -= 5
        attendance_status = f"Attendance <75%, 5 marks reduced"
    
6. Assign grades:
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "Fail"
    
7. Find failed subjects < 35:
    failed_subjects = []
    for subject, marks in subject_marks.items():
        if marks < 35:
            failed_subjects.append(subject)
    
8. Pass/Fail result: Fail if any subject <35:
    result = "Fail" if failed_subjects else "Pass"
    
    return {
        "student_id": student_id,
        "student_name": student_name,
        "total_marks": total_marks,
        "average": round(average, 1),
        "grade": grade,
        "attendance_status": attendance_status,
        "failed_subjects": failed_subjects,
        "result": result
    }

student_data = {
    "Math": 95,
    "Science": 88,
    "English": 76,
    "Computer": 92,
    "Physics": 34
}

report = process_student_results(
    student_id=1001,
    student_name="Alex",
    subject_marks=student_data,
    attendance_percentage=82,
    assignment_score=18,
    extracurricular_points=3
)

print(f"Student ID: {report['student_id']}")
print(f"Student Name: {report['student_name']}")
print(f"Total Marks: {report['total_marks']}")
print(f"Average: {report['average']}")
print(f"Grade: {report['grade']}")
print(f"Attendance Status: {report['attendance_status']}")
print(f"Failed Subjects: {report['failed_subjects']}")
print(f"Result: {report['result']}")