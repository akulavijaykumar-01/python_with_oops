class student:
    def __init__(self):
        self.name="harsha"
        self.marks=75
    def set(self,name,marks):
        self.name=name
        self.marks=marks
S=student()
print(S.name)
print(S.marks)
S.set("harsha",75)
print(S.name)
print(S.marks)