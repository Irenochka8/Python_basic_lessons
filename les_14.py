class ValueStudentError(Exception):

    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_exception_message(self):
        return self.message


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.gender}, {self.age}, {self.first_name}, {self.last_name}"
human = Human("Male", 35, "Jonh", "Smith")


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return f"{super().__str__()}, {self.record_book}"

student = Student("male", 27, "Tom", "Smith", "AN142")


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student_list):
        if len(self.group) > 9:
            raise ValueStudentError("Group is full")
        else:
            self.group.add(student_list)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
            else:
                return None

    def __str__(self):
        all_students = "; ".join([str(student) for student in self.group])
        return f'Number:{self.number}\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 31, 'dfg', 'yui', 'AN142')
st4 = Student('Male', 32, 'xcvb', 'dfg', 'AN142')
st5 = Student('Male', 35, 'vb', 'Jobs', 'AN142')
st6 = Student('Male', 16, 'Steve', 'dfg', 'AN142')
st7 = Student('Male', 20, 'Steve', 'kl', 'AN142')
st8 = Student('Male', 18, 'Mike', 'Jobs', 'AN142')
st9 = Student('Male', 20, 'Steve', 'kl', 'AN142')
st10 = Student('Male', 18, 'Steve', 'Jobs', 'AN142')
st11 = Student('Male', 19, 'Steven', 'Jobs', 'AN142')

gr = Group('PD1')
student_list = [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11]


try:
    for student in student_list:
        gr.add_student(student)
except ValueStudentError as err:
    print(err.get_exception_message())
    print(f"Should be 10")
print(gr)
