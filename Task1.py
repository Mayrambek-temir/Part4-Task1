class Student:
    def __init__(self, name, lastName, departament, years):
        self.name = name
        self.lastName=lastName
        self.departament=departament
        self.years=years

    def get_student_info(self):
        name=self.name
        lastName=self.lastName
        departament=self.departament
        years= self.years
        result = name, lastName + " поступил " + years + " г. на факультет " + departament
        return result

ex1 = Student('Vasya ', 'Ivanov', 'programming', '2019')
print(ex1.get_student_info())



