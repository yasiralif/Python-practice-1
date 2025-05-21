class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

# ফাংশন যেখানে একই নামে আলাদা আলাদা আচরণ
def animal_sound(animal):
    animal.sound()

c = Cat()
d = Dog()

animal_sound(c)  # Meow
animal_sound(d)  # Bark
class Shape:
    def area(self):
        print("I have no area")

class Circle(Shape):
    def area(self):
        print("Circle Area: πr²")

c = Circle()
c.area()  # Output: Circle Area: πr²
