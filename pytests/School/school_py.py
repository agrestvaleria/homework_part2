# Создайте класс Students, содержащий поля: фамилия и инициалы, номер группы,
# успеваемость (массив из пяти элементов).
#
# Создать класс School:
#
#     • Добавить возможно для добавления студентов в школу
#     • Добавить возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 5 или 6.
#     • Добавить возможность вывода учеников заданной группы
#     • Добавить возможность вывода учеников претендующих на автомат(средний балл >= 7)


class Students:

    def __init__(self, surname: str, group_number: int, estimates: list):
        self.surname = surname
        self.group_number = group_number
        self.estimates = estimates


class School:

    def __init__(self):
        self.students = list()

    def add_student(self, student):
        self.students.append(student)

    def marks(self, *marks):
        assert len(marks) > 1, 'please enter more than 1 mark'
        answer = ''
        for student in self.students:
            if all([mark in marks for mark in student.estimates]):
                answer += student.surname + ' '
        return answer

    def group(self, group):
        assert type(group) == int, 'group must be int'
        answer = ''
        for student in self.students:
            if student.group_number == group:
                answer += student.surname + ' '
        return answer

    def automat(self, automat):
        assert type(automat) == int, 'automat must be int'
        answer = ''
        students_with_automat = [
                student for student in self.students
                if sum(student.estimates) / len(student.estimates) >= automat]
        for student in students_with_automat:
            answer += student.surname + ' '
        return answer
