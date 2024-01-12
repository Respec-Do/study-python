# 학교
# 이름, 지역, 학생 수, 선생님 수
# 학교 정보 출력 메소드

# 선생님
# 이름, 과목, 학교
# 선생님이 추가될 때마다 선생님 수 1증가
# 준비된 학생들에게 해당 과목을 가르치면 학생들의 능력치 1증가
# 선생님 정보 출력 메소드

# 학생
# 이름, 학년(grade), 학교, 능력치(초기값: 0), 담임 선생님
# 학생이 추가될 때마다, 학생 수 1증가
# 학생 정보 출력 메소드

class School:
    def __init__(self, name, location, student_num = 0, teacher_num = 0):
        self.name = name
        self.location = location
        self.student_num = student_num
        self.teacher_num = teacher_num

    def print_school_info(self):
        print("Name: " + self.name + "\nLocation: " + self.location +\
              "\nStudents: " + str(self.student_num) + "\nTeachers: " + str(self.teacher_num))


class Teacher:
    def __init__(self, name, subject, school):
        self.name = name
        self.subject = subject
        school.teacher_num += 1

    def teaching(self, student):
        student.ability += 1


    def print_teacher_info(self):
        print("Name: " + self.name + "\nSubject: " + self.subject + "\nLocation: " + school.location)
# 학생
# 이름, 학년(grade), 학교, 능력치(초기값: 0), 담임 선생님
# 학생이 추가될 때마다, 학생 수 1증가
# 학생 정보 출력 메소드
class Student:
    def __init__(self, name, grade, school, teacher, ability=0):
        self.name = name
        self.grade = grade
        self.ability = ability
        self.school = school
        self.teacher = teacher
        self.school.student_num += 1

    def print_student_info(self):
        print("Name: " + self.name + "\nSchool: " + school.name +\
              "\nGrade: " + str(self.grade) + "\nTeachers: " + teacher.name +\
              "\nAbility: " + str(self.ability) )

school = School("역삼고", "역삼")
school.print_school_info()
print()
teacher = Teacher("Chris", "English", school)
teacher.print_teacher_info()
print()
school.print_school_info()
print()
student = Student("도강현", 1, school, teacher)
student.print_student_info()
print()
school.print_school_info()
print()
teacher.teaching(student)
student.print_student_info()
print()
school.print_school_info()
print()
teacher1 = Teacher("이수학", "Math", school)
teacher1.print_teacher_info()
print()
school.print_school_info()
student1 = Student("김규산", 2, school, teacher1)
student1.print_student_info()
school.print_school_info()