class Student:

    average_score = 0

    def __init__(self, name, age, class_):
        self.name = name
        self.age = age
        self.class_ = class_
    
    def calc_avg_score(self, t_1, t_2, t_3):
        return (t_1 + t_2 + t_3) / 3


if __name__ == "__main__":
    student_01 = Student("John", 20, "Class A")
    student_02 = Student("Martin", 18, "Class B")

    student_02_age = student_02.age
    print(student_02_age)

    student_02_avg = student_02.calc_avg_score(75, 89, 64)
    print(student_02_avg)

