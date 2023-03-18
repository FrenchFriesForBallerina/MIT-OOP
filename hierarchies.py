class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    def __str__(self):
        return "animal:" + str(self.name) + ":" + str(self.age)


class Cat(Animal):
    def speak(self):
        print("meow")

    def __str__(self):
        return "cat:" + str(self.name) + ":" + str(self.age)


class Rabbit(Animal):
    def speak(self):
        print("meep")

    def __str__(self):
        return "rabbit:" + str(self.name) + ":" + str(self.age)


class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def add_friends(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        print('howdy')

    def age_diff(self, other):
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(self.name + " is " + str(diff) +
                  " years older than " + other.name)
        else:
            print(self.name + " is " + str(-diff) +
                  " years younger than " + other.name)

    def __str__(self):
        return "person:" + str(self.name) + ":" + str(self.age)


jelly = Cat(1)
print(jelly.get_age())
jelly.set_name('Jelly')
print(jelly.get_name())
print(jelly)
print(Animal.__str__(jelly))
jelly.speak()

molly = Rabbit(3)
molly.set_name('Molly')
molly.set_age(2)
molly.speak()

peter = Person('Peter', 72)
print(peter.get_age())
peter.age_diff(molly)
peter.age_diff(jelly)

jelly.set_age(99)
peter.age_diff(jelly)
peter.add_friends(jelly)
peter.add_friends(molly)
friends = peter.get_friends()
print(str(friends))
