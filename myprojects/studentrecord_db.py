import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "student_management"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE student_management")

sql = """ CREATE TABLE students (
  id INT NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(30) NOT NULL,
  last_name VARCHAR(30) NOT NULL,
  age INT NOT NULL CHECK(age>=17),
  gender VARCHAR(1) NOT NULL,
  gpa DECIMAL(2,2),
  PRIMARY KEY (id)
)"""

def add_student(first_name, last_name, age, gender):
    sql = """ INSERT INTO students(first_name, last_name, age, gender, gpa)
    VALUES (%s, %s, %s, %s, NULL)
    """
    stud =  (first_name, last_name, age, gender)

    mycursor.execute(sql, stud)
    mydb.commit()
    # print("Student added successfully!")


def search_student(id):
    sql = "SELECT * FROM students WHERE id = %s"
    stud_id = (id,)

    mycursor.execute(sql, stud_id)
    return mycursor.fetchone()  
    
    # if myresult:
    #     print(myresult)
    # else:
    #     print("Student ID not found!")    
    

def view_student():
    sql = "SELECT * FROM students"

    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    

    for r in myresult:
        print(r)

def student_exists(id):
    sql = "SELECT * FROM students WHERE id = %s"
    stud = (id,)

    mycursor.execute(sql, stud)
    myresult = mycursor.fetchone()
    return myresult is not None

def update_student(id, first_name, last_name, age, gender, gpa):
    sql = """UPDATE students  
    SET first_name = %s,
        last_name = %s,
        age = %s,
        gender = %s,
        gpa = %s
    WHERE id = %s"""

    stud = (first_name, last_name, age, gender, gpa, id)

    mycursor.execute(sql, stud)
    mydb.commit()
    return mycursor.rowcount > 0

def delete_student(id):
    sql = "DELETE FROM students WHERE id = %s"
    stud = (id,)

    mycursor.execute(sql, stud)
    mydb.commit()
    return mycursor.rowcount > 0
    # if myresult:
    #     print()
    # for r in myresult:
    #     print(r)

# add_student("lawal", "sultan", 21, "M", 4.10)    
# search_student(1)