# thsi is encapsulation 

class fish:
    def __init__(self):
        self._size = "big"
    def get_size(self):
        print("I am "+self._size + " fish")
    def set_size(self, new_size):
        self._size = new_size
        print("I am "+new_size +" ish")

o = fish()
o.get_size()

#change value 
o._size=('small')
o.get_size()
#new size change 
p = fish()
p.set_size(" fini")
