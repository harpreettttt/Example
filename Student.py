class Student: #creating the constructor but only include the name and student id in the class as courses and grades need to be empty
    def __init__(self, name: str, student_id: int):
        self.name = name # name
        self.student_id = student_id #id
        self.courses = [] #courses in array so we can append and add
        self.grades = {} # grades are in dictionary

    def enroll(self, course_name:str): #adding course names to the array if its not already present
        if course_name in self.courses: # if the course exists
           pass
        else:
            self.courses.append(course_name) #add to the list
            return True #confirms course enrolment

    def add_grade(self,course_name:str,grade:float): #creating method to add the grade to the course after it has been found
        if course_name in self.courses: #if the course name is in the courses
            self.grades[course_name] = grade #add/update grades
            return True #shows the grades has been added/updated
        else: #only adds grade after student is enrolled onto the course
            raise ValueError("Student is not enrolled in the course.")

    def get_gpa(self):
        if len(self.grades) == 0: #len finds the length of a dictionary
            return None
        total=sum(self.grades.values()) #calculate total of all grades and then divide to find the average. (GPA)
        average= total / len(self.grades)
        return average

    def __str__(self):
        return f"Student Name: {self.name}, ID: {self.student_id}, Courses: {self.courses}"


