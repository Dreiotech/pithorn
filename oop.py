class Fruits:
    def __init__(self,name,price,colour):
        self.name=name
        self.price=price
        self.colour=colour
    def onyesha(self):
         print(f"My favourite fruit is {self.name}"
               f" and its cost Ksh.{self.price}"
               f" and it is {self.colour} in colour")

myobj=Fruits(name="Oranges",price=50,colour="Orange")
myobj.onyesha()
myobj2=Fruits(name="Strawberry",price=70,colour="Red")
myobj2.onyesha()
myobj3=Fruits(name="Apples",price=40,colour='Green')
myobj3.onyesha()