import re

text = "Amar nam Yasir Arafat Alif"

# 'Yasir' শব্দটা আছে কি না সেটা খোঁজো
match = re.search(r"Yasir", text)

if match:
    print("Word found!")
else:
    print("Not found.")
x = re.findall("a" ,text)
print(x.count('a'))
