"""
7. Using inheritance, construct a class system for
"University", with subclasses like "Faculty", "Students", "Courses", and "Departments";
include attributes and methods suitable to each class.
"""


class University:
    def __init__(self, name):
        self.name = name

    def get_address(self):
        print("{} is based in Bolpur.".format(self.name))


class Faculty(University):
    """
    In the example code, super().__init__.py(name) is called
    in both 'Faculty' and 'Students' subclasses
    to execute the __init__.py method from the parent class 'University'.
    This allows to set the 'name' attribute in 'Faculty' and 'Students' classes
    based on the 'University' class definition.
    Thereby, super allows us to avoid writing duplicate code
    and supports the concept of code reusability.
    """
    def __init__(self, name, faculty_name):
        super().__init__(name)
        self.faculty_name = faculty_name

    # def get_address(self):
    #     print("{} is located in Bolpur.".format(self.name))


class Students(University):
    def __init__(self, name, student_name):
        super().__init__(name)
        self.student_name = student_name


class Courses(University):
    pass


university = University('Viswabharati')
faculty = Faculty('Bidhan Chandra Krishi Vidyalaya', 'Naren Dutta')
student = Students('Seacom Skills University', 'Dipanjan Das')
print("University:\t", university.name)
print("Faculty University:\t", faculty.name)
print("Faculty Name:\t", faculty.faculty_name)
print("Student University:\t", student.name)
print("Student Name:\t", student.student_name)

faculty.get_address()
print(faculty.__doc__)
