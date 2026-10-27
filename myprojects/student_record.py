import studentrecord_db
import coursestb_db
import student_coursesdb

class Student:
    def __init__(self, first_name, last_name, age, gender, gpa, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.gpa = gpa
        self.id = id

    def display_info(self):
        print(f"\nStudent ID: {self.id}")
        print(f"First Name: {self.first_name}") 
        print(f"Last Name: {self.last_name}") 
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"GPA: {self.gpa}")




class StudentManagement:
    def __init__(self):
        pass

    def view_student(self):    
        studentrecord_db.view_student()


    def add_student(self):
        first_name = input("Enter your First Name: ").capitalize()
        last_name = input("Enter your Last Name: ").capitalize()
        age = int(input("Enter your Age: "))
        gender = input("Enter your Gender. (m/f): ").upper()
        



        studentrecord_db.add_student(first_name, last_name, age, gender)

        print("\nStudent added successfully!")
        

    def remove_student(self):
        remove_id = int(input("Enter the student ID to remove: "))
        
        found = studentrecord_db.delete_student(remove_id)
        
        if found:        
            print("\nStudent removed successfully!")
        else:
            print("\nStudent ID not found!")    
        
    
    def update_student(self):
        update_id = int(input("Enter ID to update: "))
        check = studentrecord_db.student_exists(update_id)

        if not check:
            print("\nStudent ID not found!")
            return

        new_first_name = input("\nEnter new First Name: ").capitalize()
        new_last_name = input("Enter new Last Name: ").capitalize()
        new_age = int(input("Enter new Age: "))
        new_gender = input("Enter new Gender. (m/f): ").upper()
        
        
        success = studentrecord_db.update_student(update_id, new_first_name, new_last_name, new_age, new_gender)
            
        if success:    
            print("\nStudent updated successfully!")
            


    def search_student(self):
        search_id = int(input("Enter student ID: "))
        found = studentrecord_db.search_student(search_id)

        if found:
            print(found)
        else:
            print("\nStudent ID not found!") 


    # courses section
    def add_courses(self):
        
        course_code = input("Enter your course code (e.g. MTH101): ").upper()
        course_name = input("Enter your course name: ").upper()
        credit_unit = int(input("Enter course unit (e.g. 1-6): "))


        success = coursestb_db.add_courses(course_code, course_name, credit_unit)

        print("\nStudent course added successfully!")


    def update_courses(self):
        course_id = int(input("Enter course ID to update course: "))
        check = coursestb_db.id_exist(course_id)

        if not check:
            print("\nStudent ID not found!")
            return
        
        new_course_code = input("Enter new course code (e.g. MTH101): ").upper()
        new_course_name = input("Enter new course name: ").capitalize()
        new_credit_unit = int(input("Enter new course unit (e.g. 1-6): "))

        success = coursestb_db.update_courses(course_id, new_course_code, new_course_name, new_credit_unit)

        if success:
            print("\nStudent course updated successfully!")


    def remove_courses(self):
        student_id = int(input("Enter student ID to remove course: "))
        found = coursestb_db.delete_course(student_id)

        if found:
            print("\nStudent course removed successfully!") 
        else:
            print("\nStudent ID not found!")

    
    def search_courses(self):
        student_id = int(input("Enter student ID to search: "))
        found = coursestb_db.search_course(student_id)

        if found:
            print(found)
        else:
            print("\nStudent ID not found!")    
    

    def view_courses(self):
        coursestb_db.view_course()


    # Enroll section
    def enroll(self):
        student_id = int(input("Enter student ID to enroll: "))

        check = studentrecord_db.student_exists(student_id)

        if not check:
            print("\nStudent ID not found!")
            return
        
        course_id = int(input("Enter course ID: "))
        score = int(input("Enter your course score: "))
        semester = input("Enter semester (e.g. Rain/Harmattan): ").capitalize()
        academic_year = input("Enter session (e.g. YYYY/YYYY): ")

        success = student_coursesdb.add_enroll(student_id, course_id, score, semester, academic_year)

        if success:
            print("\nStudent registered successfully!")

    def update_score(self):
        student_id = int(input("Enter student ID: "))

        check = studentrecord_db.student_exists(student_id)

        if not check:
            print("\nStudent ID not found!")
            return
        
        course_id = int(input("Enter course ID: "))
        new_score = int(input("Enter new score: "))

        success = student_coursesdb.update_score(student_id, course_id, new_score)

        if success:
            print("\nCourse updated successfully!")

    def calc_gpa(self):
        student_id = int(input("Enter student ID: "))

        check = studentrecord_db.student_exists(student_id)

        if not check:
            print("\nStudent ID not found!")
            return
        
        gpa = student_coursesdb.calculate_gpq(student_id)

        if gpa is None:
            print("\nThis student has not registered for any courses!")
        else:
            print(f"\nStudent GPA: {gpa}")    




    # Option section
    def option(self):
       while True:

        print("\n----- Student Record Management System -----")

        print("1. Add Student")
        print("2. Search Student by ID")
        print("3. Remove Student")
        print("4. Update Student")
        print("5. View Student")

        print("\n<----Courses Section---->")
        print("6. Add Student Course")
        print("7. Search Student Course by ID")
        print("8. Remove Student Course")
        print("9. Update Student Course")
        print("10. Register Student for Course")

        print("\n<----Score Section---->")
        print("11. Update Student Score")
        print("12. Calculate GPA")

        print("13. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            self.add_student()

        elif choice == "2":
            self.search_student()

        elif choice == "3":
            self.remove_student()

        elif choice == "4":
            self.update_student()

        elif choice == "5":
            self.view_student()

        elif choice == "6":
            self.add_courses()

        elif choice == "7":
            self.search_courses()

        elif choice == "8":
            self.remove_courses()

        elif choice == "9":
            self.update_courses()

        elif choice == "10":
            self.enroll()

        elif choice == "11":
            self.update_score()

        elif choice == "12":
            self.calc_gpa()        

        elif choice == "13":
            print("Exiting....")
            break

        else:
            print("Invalid choice. Please try again!")
            



    


st1 = StudentManagement()
# st1.add_student()
# st1.view_student()
st1.option()


