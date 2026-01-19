class Parrot:
    def __init__(self,name,age):
        self.age = age
        self.name = name

    def sing(self,song):
        return "{} sings {}". format(self.name,song)
    
    def dance(self):
        return "{} is now dancing".format(self.name)
    
blu = Parrot("Blu", 10)

print(blu.sing("Happy")) #Happy refers to the song
print(blu.dance)