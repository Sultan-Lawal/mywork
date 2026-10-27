import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "student_management"
)

mycursor = mydb.cursor()


sql = """CREATE TABLE courses (
  id INT NOT NULL AUTO_INCREMENT,
  course_code VARCHAR(10) NOT NULL UNIQUE,
  course_name VARCHAR(100) NOT NULL,
  credit_unit INT NOT NULL,
  PRIMARY KEY(id)
)"""

def add_courses(course_code, course_name, credit_unit):
    sql = """ INSERT INTO courses(course_code, course_name, credit_unit)
    VALUES(%s, %s, %s)
    """
    course = (course_code, course_name, credit_unit)

    mycursor.execute(sql, course)
    mydb.commit()
    return mycursor.rowcount > 0

def update_courses(id, course_code, course_name, credit_unit):
    sql = """UPDATE courses
    SET course_code = %s,
        course_name = %s,
        credit_unit = %s
    WHERE id = %s"""    

    course = (course_code, course_name, credit_unit, id)

    mycursor.execute(sql, course)
    mydb.commit()
    return mycursor.rowcount > 0

def delete_course(id):
    sql = "DELETE FROM courses WHERE id = %s"
    course = (id,)

    mycursor.execute(sql, course)
    mydb.commit()
    return mycursor.rowcount > 0

def search_course(id):
    sql = "SELECT * FROM courses WHERE id = %s"
    course = (id,)

    mycursor.execute(sql, course)
    return mycursor.fetchone()

def view_course():
    sql = "SELECT * FROM courses"

    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    

    for r in myresult:
        print(r)

def id_exist(id):
    sql = "SELECT * FROM courses WHERE id = %s"
    cour_id = (id,)

    mycursor.execute(sql, cour_id)
    myresult = mycursor.fetchone()
    return myresult is not None

