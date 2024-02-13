class People:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"My name is  {self.name}"f" and I am {self.age} years old")

myobj=People(name="Steve",age=18)
myobj.display()
myobj2=People(name="Mbappe",age=22)
myobj2.display()
myobj3=People(name="Ivy",age=23)
myobj3.display()
myobj4=People(name="Messi",age=37)
myobj4.display()
myobj5=People(name="Serah",age=24)
myobj5.display()