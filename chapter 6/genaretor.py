# def num (n):
#     for i in range(1,n):
#         yield n
    
# a = num(4)
# next(a)
# next(a)
# next(a)
# next(a)
def num(n):
    for i in range(1, n):
        yield i

a = num(10)

print(next(a))  # 1
print(next(a))  # 2
print(next(a))  # 3
print(next(a))  # 4
