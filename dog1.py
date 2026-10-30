class Dog:
    def eat(self):
        print("Dog eats food")
class Cat:
    def eat(self):
        print("Cat eats food")
def show(eating):
    eating.eat()
show (Dog())
show (Cat())