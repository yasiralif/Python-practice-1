class MyClass:
    def __init__(self):
        self._protected_var = 20  # Protected member

obj = MyClass()
print(obj._protected_var)  # ✅ 20 (কিন্তু convention হলো: সরাসরি ব্যবহার না করা)

