# def even_numbers(n):
#     for i in range(n):
#         if i % 2 == 0:
#             yield i

# for num in even_numbers(10):
#     print(num)


def generator ():
    t = 1
    print("frist number",t)
    yield t

    t +=1
    print("decond number",t)
    yield t

call = generator()
next(call)
next(call)