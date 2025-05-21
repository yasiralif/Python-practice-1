class Animal:
    def Ani(self):
        print("animal sound")
class Dog(Animal):  # Inheriting from Animal class
    def bark(self):
        print("Dog barks")

d= Dog()
d.Ani()
d.bark()