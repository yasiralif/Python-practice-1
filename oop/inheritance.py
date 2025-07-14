
# class dog :
#     def __init__(self,name):
#         self.name= name 
#         print(f"this is my name {name}")

# spot = dog("all")


from abc import ABC, abstractmethod

# এটা হলো Abstract Base Class
class Animal(ABC):

    # এটা হলো Abstract Method (define করে রাখা, কিন্তু ভিতরে কিছু লেখা হয়নি)
    @abstractmethod
    def sound(self):
        pass

# এখন আমরা এটা ইনহেরিট করে বাস্তব ক্লাস বানাবো
class Dog(Animal):
    def sound(self):
        print("ঘেউ ঘেউ")

class Cat(Animal):
    def sound(self):
        print("মিঁউ মিঁউ")

# এখন অবজেক্ট তৈরি করে চেক করবো
d = Dog()
d.sound()   # আউটপুট: ঘেউ ঘেউ

c = Cat()
c.sound()   # আউটপুট: মিঁউ মিঁউ

