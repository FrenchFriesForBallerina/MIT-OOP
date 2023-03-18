import datetime


class Person(object):

    def __init__(self, name):
        self.name = name
        self.birthday = None
        self.lastname = name.split(' ')[-1]

    def set_birthday(self, day, month, year):
        self.birthday = datetime.date(year, month, day)

    def get_lastname(self):
        return self.lastname

    def __str__(self):
        return self.name

    def get_age(self):
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days/365

    def __lt__(self, other):
        if self.lastname == other.lastname:
            return self.name < other.name
        return self.lastname < other.lastname


class Student(Person):
    nextIDNum = 0

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = Student.nextIDNum
        Student.nextIDNum += 1

    def getIdNum(self):
        return self.idNum

    def __lt__(self, other):
        return self.idNum < other.idNum

    def __str__(self):
        return str(self.idNum)

    def speak(self, utterance):
        return (self.get_lastname() + " says: " + utterance)


p1 = Person("Martin Luckberg")
p1.set_birthday(1, 1, 2000)
print(p1.get_age())
p2 = Person('Wanya Houston')
p2.set_birthday(31, 12, 1983)
p3 = Person('Steve Gates')
p3.set_birthday(10, 10, 1910)
p4 = Person('Jane Anaconda')
p4.set_birthday(8, 3, 1957)
p5 = Person('Maria Gates')
p5.set_birthday(10, 10, 1910)

personList = [p1, p2, p3, p4, p5]

print(p2.__lt__(p1))

for e in personList:
    print(e)

print('')
personList.sort()

for e in personList:
    print(e)


student1 = Student("Cecilia")
student2 = Student("Bruno")
student3 = Student("Alberto")

studentList = [student3, student2, student1]
for e in studentList:
    print(e.getIdNum())

studentList.sort()
print('')

for e in studentList:
    print(e)
