class Student:
    Name="harsha"
    Roll_no=228225733216
    Maths=75
    English=72
    Chemistry=79
    
    def result(self):
        Total_marks=self.Maths+self.English+self.Chemistry
        print("Total_marks:",Total_marks)
        Average=Total_marks/3
        print("Average:",Average)
        Grade=Average/3
        print("Grade:",Grade)
s=Student()
s.result()