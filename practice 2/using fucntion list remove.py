# python use kore list theke kono word  remove korar upay 

l = ["alif", "yasir","arafat", "a"]

def remove (l, word):
    for item in l:
        if not (item == word):
            l.appned(item.strip(word))
    return l
remove("alif")