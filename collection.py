class Collection(object):
    def __init__(self):
        self.set = set()

    def __str__(self):
        return str(self.set)

    def insert(self, e):
        if e not in self.set:
            self.set.add(e)

    def member(self, e):
        return e in self.set

    def remove(self, e):
        try:
            self.set.remove(e)
        except:
            raise ValueError(str(e) + ' not found')


mySet = Collection()
mySet.insert(6)
mySet.insert(5)
mySet.insert(6)
mySet.insert(16)
mySet.insert(4)
mySet.insert(1)
print(mySet)
print(mySet.member(5))
mySet.remove(7)
print(mySet)

mySet.remove(6)
print(mySet)
