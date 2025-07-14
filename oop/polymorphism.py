# class Cat:
#     def sound(self):
#         print("Meow")

# class Dog:
#     def sound(self):
#         print("Bark")

# # ফাংশন যেখানে একই নামে আলাদা আলাদা আচরণ
# def animal_sound(animal):
#     animal.sound()

# c = Cat()
# d = Dog()

# animal_sound(c)  # Meow
# animal_sound(d)  # Bark
# class Shape:
#     def area(self):
#         print("I have no area")

# class Circle(Shape):
#     def area(self):
#         print("Circle Area: πr²")

# c = Circle()
# c.area()  # Output: Circle Area: πr²

# polymorphsim diye akta main class theke child class yar sob kisu access newa jai
class main:
    def __init__(self, name , id, dep, semester):
        self.name= name
        self.id = id
        self.dep= dep
        
        self.semester = semester
    
class student1 (main):
    pass
s1= student1("alif",848205,"cmt","3rd")

print(f"My name is {s1.name} my id is {s1.id} and my dep is {s1.dep} and my ")
