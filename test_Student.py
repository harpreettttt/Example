# test_Student.py

import unittest
from Student import Student


studentTestPass = False

class TestStudent(unittest.TestCase):
    def setUp(self):
        """
        Set up a Student object for testing.
        This method is called before each test.
        """
        self.student = Student(name="John Doe", student_id=1001)

    def test_initialization(self):
        """
        Test that the Student object is initialized correctly.
        """
        self.assertEqual(self.student.name, "John Doe")
        self.assertEqual(self.student.student_id, 1001)
        self.assertEqual(self.student.courses, [])
        self.assertEqual(self.student.grades, {})
        studentTestPass = True


    def test_enroll_new_course(self):
        """
        Test enrolling in a new course.
        """
        self.student.enroll("Biology")
        self.assertIn("Biology", self.student.courses)
        self.assertEqual(len(self.student.courses), 1)

    def test_enroll_duplicate_course(self):
        """
        Test that enrolling in a duplicate course does not add it again.
        """
        self.student.enroll("Chemistry")
        self.student.enroll("Chemistry")  # Attempt to enroll again
        self.assertIn("Chemistry", self.student.courses)
        self.assertEqual(len(self.student.courses), 1)  # Should still be only one course

    def test_add_grade_enrolled_course(self):
        """
        Test adding a grade for an enrolled course.
        """
        self.student.enroll("Mathematics")
        self.student.add_grade("Mathematics", 95.0)
        self.assertIn("Mathematics", self.student.grades)
        self.assertEqual(self.student.grades["Mathematics"], 95.0)

    def test_add_grade_not_enrolled_course(self):
        """
        Test that adding a grade for a course the student is not enrolled in raises ValueError.
        """
        with self.assertRaises(ValueError) as context:
            self.student.add_grade("Physics", 88.0)
        self.assertEqual(str(context.exception), "Student is not enrolled in the course.")

    def test_get_gpa_no_grades(self):
        """
        Test that get_gpa returns None when there are no grades.
        """
        self.assertIsNone(self.student.get_gpa())

    def test_get_gpa_with_grades(self):
        """
        Test that get_gpa correctly calculates the GPA with existing grades.
        """
        self.student.enroll("History")
        self.student.enroll("Geography")
        self.student.add_grade("History", 80.0)
        self.student.add_grade("Geography", 90.0)
        expected_gpa = (80.0 + 90.0) / 2
        self.assertEqual(self.student.get_gpa(), expected_gpa)

    def test_str_representation(self):
        """
        Test the string representation of the Student object.
        """
        self.student.enroll("Art")
        expected_str = "Student Name: John Doe, ID: 1001, Courses: ['Art']"
        self.assertEqual(str(self.student), expected_str)

    def test_multiple_enrollments_and_grades(self):
        """
        Test multiple enrollments and adding multiple grades.
        """
        courses = ["English", "Physics", "Chemistry"]
        grades = {"English": 85.0, "Physics": 90.0, "Chemistry": 78.0}

        for course in courses:
            self.student.enroll(course)

        for course, grade in grades.items():
            self.student.add_grade(course, grade)

        self.assertEqual(set(self.student.courses), set(courses))
        self.assertEqual(self.student.grades, grades)
        expected_gpa = sum(grades.values()) / len(grades)
        self.assertEqual(self.student.get_gpa(), expected_gpa)
        print("Final test PASSED")




# To run the tests, uncomment the following lines:
if __name__ == '__main__':
     unittest.main()
