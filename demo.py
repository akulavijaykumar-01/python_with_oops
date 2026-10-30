class Demo:
    def add(self, a=0, b=0):
        print("Sum =", a + b)


d = Demo()

d.add()
d.add(10)
d.add(10, 20)