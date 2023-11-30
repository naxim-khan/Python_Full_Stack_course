class Animal:
    def __init__(self):
        self.num_eyes=2
        
    def breathe(self):
        print("Inhale. Exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()
    def breathe(self):
        super().breathe()
        print("Doing this underwater")
    def swim(self):
        print("Moving Under water")


trout=Fish()
trout.breathe()
trout.swim()
print(trout.num_eyes)