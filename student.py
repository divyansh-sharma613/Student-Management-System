import json


class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.attendance = 0
        self.marks = {}

    def add_attendance(self, attendance):
        self.attendance = attendance

    def add_marks(self, subject, marks):
        self.marks[subject] = marks

    def total_marks(self):
        return sum(self.marks.values())

    def percentage(self):
        if len(self.marks) == 0:
            return 0

        return self.total_marks() / len(self.marks)

    def grade(self):
        percentage = self.percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "attendance": self.attendance,
            "marks": self.marks
        }


class StudentManagementSystem:

    def __init__(self):
        self.file_name = "students.json"
        self.students = {}
        self.load_data()

    # Load data from file
    def load_data(self):
        try:
            with open(self.file_name, "r") as file:
                data = json.load(file)

                for student_id, info in data.items():
                    student = Student(
                        info["student_id"],
                        info["name"],
                        info["age"],
                        info["course"]
                    )

                    student.attendance = info["attendance"]
                    student.marks = info["marks"]

                    self.students[student_id] = student

        except FileNotFoundError:
            self.students = {}

    # Save data to file
    def save_data(self):
        data = {}

        for student_id, student in self.students.items():
            data[student_id] = student.to_dict()

        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=4)

    # Add student
    def add_student(self):
        print("\n---------- ADD STUDENT ----------")

        student_id = input("Enter Student ID: ")

        if student_id in self.students:
            print("Student ID already exists!")
            return

        name = input("Enter Student Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course/Class: ")

        student = Student(student_id, name, age, course)

        self.students[student_id] = student
        self.save_data()

        print("Student added successfully!")

    # View all students
    def view_students(self):
        print("\n---------- ALL STUDENTS ----------")

        if len(self.students) == 0:
            print("No students found.")
            return

        for student in self.students.values():
            print("--------------------------------")
            print("Student ID :", student.student_id)
            print("Name       :", student.name)
            print("Age        :", student.age)
            print("Course     :", student.course)
            print("Attendance :", student.attendance, "%")
            print("Marks      :", student.marks)

    # Search student
    def search_student(self):
        print("\n---------- SEARCH STUDENT ----------")

        student_id = input("Enter Student ID: ")

        if student_id not in self.students:
            print("Student not found!")
            return

        student = self.students[student_id]

        print("\nStudent Found")
        print("--------------------------")
        print("Student ID :", student.student_id)
        print("Name       :", student.name)
        print("Age        :", student.age)
        print("Course     :", student.course)
        print("Attendance :", student.attendance, "%")
        print("Marks      :", student.marks)

    # Update student
    def update_student(self):
        print("\n---------- UPDATE STUDENT ----------")

        student_id = input("Enter Student ID: ")

        if student_id not in self.students:
            print("Student not found!")
            return

        student = self.students[student_id]

        print("1. Update Name")
        print("2. Update Age")
        print("3. Update Course")

        choice = input("Enter choice: ")

        if choice == "1":
            student.name = input("Enter new name: ")

        elif choice == "2":
            student.age = input("Enter new age: ")

        elif choice == "3":
            student.course = input("Enter new course: ")

        else:
            print("Invalid choice!")
            return

        self.save_data()

        print("Student updated successfully!")

    # Delete student
    def delete_student(self):
        print("\n---------- DELETE STUDENT ----------")

        student_id = input("Enter Student ID: ")

        if student_id not in self.students:
            print("Student not found!")
            return

        del self.students[student_id]
        self.save_data()

        print("Student deleted successfully!")

    # Add attendance
    def add_attendance(self):
        print("\n---------- ATTENDANCE ----------")

        student_id = input("Enter Student ID: ")

        if student_id not in self.students:
            print("Student not found!")
            return

        try:
            attendance = float(input("Enter attendance percentage: "))

            if attendance < 0 or attendance > 100:
                print("Attendance must be between 0 and 100.")
                return

            self.students[student_id].add_attendance(attendance)
            self.save_data()

            print("Attendance added successfully!")

        except ValueError:
            print("Please enter a valid number.")

    # Add marks
    def add_marks(self):
        print("\n---------- ADD MARKS ----------")

        student_id = input("Enter Student ID: ")

        if student_id not in self.students:
            print("Student not found!")
            return

        subject = input("Enter Subject: ")

        try:
            marks = float(input("Enter marks out of 100: "))

            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100.")
                return

            self.students[student_id].add_marks(subject, marks)
            self.save_data()

            print("Marks added successfully!")

        except ValueError:
            print("Please enter a valid number.")

    # Generate report card
    def generate_report_card(self):
        print("\n---------- REPORT CARD ----------")

        student_id = input("Enter Student ID: ")

        if student_id not in self.students:
            print("Student not found!")
            return

        student = self.students[student_id]

        print("\n========================================")
        print("             REPORT CARD")
        print("========================================")
        print("Student ID :", student.student_id)
        print("Name       :", student.name)
        print("Age        :", student.age)
        print("Course     :", student.course)
        print("----------------------------------------")

        print("Attendance :", student.attendance, "%")

        print("\nSubject-wise Marks:")

        if len(student.marks) == 0:
            print("No marks available.")
        else:
            for subject, marks in student.marks.items():
                print(subject, ":", marks)

            print("----------------------------------------")
            print("Total Marks :", student.total_marks())
            print("Percentage  :", round(student.percentage(), 2), "%")
            print("Grade       :", student.grade())

        print("========================================")

    # Main menu
    def menu(self):

        while True:

            print("\n")
            print("========================================")
            print("       STUDENT MANAGEMENT SYSTEM")
            print("========================================")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Add Attendance")
            print("7. Add Marks")
            print("8. Generate Report Card")
            print("9. Exit")
            print("========================================")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.view_students()

            elif choice == "3":
                self.search_student()

            elif choice == "4":
                self.update_student()

            elif choice == "5":
                self.delete_student()

            elif choice == "6":
                self.add_attendance()

            elif choice == "7":
                self.add_marks()

            elif choice == "8":
                self.generate_report_card()

            elif choice == "9":
                print("\nThank you for using Student Management System!")
                break

            else:
                print("Invalid choice! Please try again.")


# Start the program
system = StudentManagementSystem()
system.menu()