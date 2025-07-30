# Student Record Manager 

students = []  # Global list to hold student records

def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    student = {
        'roll': roll_no,
        'name': name,
        'marks': marks
    }

    students.append(student)
    print("✅ Student added successfully!")

def view_students():
    if not students:
        print("📭 No student records found.")
    else:
        print("\n📋 List of Students:")
        for idx, student in enumerate(students, start=1):
            print(f"{idx}. Roll: {student['roll']}, Name: {student['name']}, Marks: {student['marks']}")
            

def search_student(roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            print("Student found:")
            print("Name:", student["name"])
            print("roll_no:", student["roll_no"])
            print("Marks:", student["marks"])
            return
    print("Student not found.")


def update_student(roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            print("Current details:")
            print("Name:", student["name"])
            print("Roll No:", student["roll_no"])
            print("Marks:", student["marks"])

            student["name"] = input("Enter new name: ")
            student["marks"] = int(input("Enter new marks: "))
            print("Student details updated.")
            return
    print("Student not found.")

def delete_student(roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("Student deleted successfully.")
            return
    print("Student not found.")
    

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        roll_no = input("Enter roll number: ")
        marks = int(input("Enter marks: "))
        students.append({"name": name, "roll_no": roll_no, "marks": marks})
    elif choice == "2":
        for student in students:
            print(student)
    elif choice == "3":
        roll_no = input("Enter roll number to search: ")
        search_student(roll_no)
    elif choice == "4":
        roll_no = input("Enter roll number to update: ")
        update_student(roll_no)
    elif choice == "5":
        roll_no = input("Enter roll number to delete: ")
        delete_student(roll_no)
    elif choice == "6":
        break
    else:
        print("Invalid choice. Try again.")
    
    


    
        
