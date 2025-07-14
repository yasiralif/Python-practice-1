# class aliff:
#     name = "alif"
#     age= '30'

#     def details(self):
#         print("you are 18 ")

# my_details = aliff()

# print(f"this is my name {my_details.name}  & My age is {my_details.age}")


class Car:
    def details (self, brand, color):
        self.brand = brand
        self.color = color

    def display_info(self):
        print(f"Brand: {self.brand}, Color: {self.color}")

# ভিন্ন ভিন্ন অ্যাট্রিবিউট দিয়ে অবজেক্ট তৈরি
car1 = Car("Honda", "Blue")
car2 = Car("Ford", "Black")

car1.display_info()  # আউটপুট: Brand: Honda, Color: Blue
car2.display_info()  # আউটপুট: Brand: Ford, Color: Black

