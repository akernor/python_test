# first test
# class Person:
#     name = "Ivan"
#     age = 10
#
#     def set(self, name, age):
#         self.name = name
#         self.age = age
#
#
# vlad = Person()
# vlad.set("Влад", 25)
# print(vlad.name + " " + str(vlad.age))
#
# ivan = Person()
# ivan.set("Иван", 56)
# print(ivan.age)
#
# kolya = Person()
# kolya.set(kolya.name, kolya.age)
# print(kolya.name + " " + str(kolya.age))



# secont test
class User:
    def setName(self, n):
        self.name = n

    def getName(self):
        try:
            return self.name
        except:
            print("No name")


first = User()
second = User()

first.setName("Bob")

print(first.getName())
print(second.getName())