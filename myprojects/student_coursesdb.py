import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "student_management"
)

mycursor = mydb.cursor()

sql = """ CREATE TABLE enrollments (
  id INT AUTO_INCREMENT PRIMARY KEY,
  student_id INT NOT NULL,
  course_id INT NOT NULL,
  score DECIMAL(5,2),
  semester VARCHAR(20),
  academic_year VARCHAR(20), 

  FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
  FOREIGN KEY (course_id) REFERENCES courses(id)
);"""

def add_enroll(student_id, course_id, score, semester, academic_year):
    sql = """ INSERT INTO enrollments(student_id, course_id, score, semester, academic_year)
    VALUES(%s, %s, %s, %s, %s)
    """
    enroll = (student_id, course_id, score, semester, academic_year)

    mycursor.execute(sql, enroll)
    mydb.commit()
    return mycursor.rowcount > 0


def update_score(student_id, course_id, new_score):
    sql = """UPDATE enrollments
    SET score = %s
    WHERE student_id = %s
    AND course_id = %s;
    """    
    score = (new_score, student_id, course_id)

    mycursor.execute(sql, score)
    mydb.commit()
    return mycursor.rowcount > 0

def calculate_gpq(student_id):
    sql = """SELECT
      e.score, c.credit_unit
    FROM enrollments e
    JOIN courses c
    ON e.course_id = c.id
    WHERE e.student_id = %s;
    """
    
    values = (student_id,)

    mycursor.execute(sql, values)
    rows = mycursor.fetchall()
    
    total_quality_points = 0
    total_credit_units = 0

    for score, credit_unit in rows:
        gp = grade_point(score)

        total_quality_points += gp * credit_unit
        total_credit_units += credit_unit

    if total_credit_units == 0:
        return None
        
    gpa = total_quality_points / total_credit_units


    sql = """UPDATE students
    SET gpa = %s
    WHERE id = %s
    """

    values = (gpa, student_id)
    mycursor.execute(sql, values)
    mydb.commit()

    return round(gpa, 2)


    


def grade_point(score):
    if score >= 70:
        return 5
    elif score >= 60:
        return 4
    elif score >= 50:
        return 3
    elif score >= 45:
        return 2
    elif score >= 40:
        return 1
    else:
        return 0

