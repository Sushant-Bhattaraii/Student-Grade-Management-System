class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def calculate_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def display_info(self):
        print(f"ID: {self.student_id} | Name: {self.name} | Avg Grade: {self.calculate_average():.2f}")

class GradeManagementSystem:
    def __init__(self):
        self.students = {}
    
    def add_student(self, name, student_id):
        if student_id in self.students:
            print("Error: Student ID already exists!")
        else:
            self.students[student_id] = Student(name, student_id)
            print("Student added!")
    
    def add_grade(self, student_id, grade):
        if student_id in self.students:
            self.students[student_id].add_grade(grade)
            print("Grade added!")
        else:
            print("Error: Student not found!")
    
    def display_all_students(self):
        if not self.students:
            print("No students in the system.")
        else:
            for student in self.students.values():
                student.display_info()

if __name__ == "__main__":
    system = GradeManagementSystem()
    
    while True:
        print("\n1. Add Student\n2. Add Grade\n3. Display All Students\n4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            name = input("Student Name: ")
            student_id = input("Student ID: ")
            system.add_student(name, student_id)
        elif choice == "2":
            student_id = input("Student ID: ")
            try:
                grade = float(input("Enter Grade: "))
                system.add_grade(student_id, grade)
            except ValueError:
                print("Error: Invalid grade format!")
        elif choice == "3":
            system.display_all_students()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")
