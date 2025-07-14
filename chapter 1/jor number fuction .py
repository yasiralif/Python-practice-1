
def even_sum(n):
    total = 0
    for i in range(1, 101):
        if i % 2 == 0:
            total += i
    return total

# ফাংশন কল করা
result = even_sum()
print("১ থেকে ১০০ পর্যন্ত জোড় সংখ্যার যোগফল:", result)
