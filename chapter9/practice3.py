# create class Student that takes 3 marks and has a method average().

class student:
    def __init__(self,name,list0Marks):
        self.name=name
        self.list0Masks=list0Marks

    def average(self):
        sum=0
        for each in self.list0Masks:
            sum=sum+each

        avg=sum/3

        print("Average is :",avg)

 
student1= student ("subh", [98,99,99])
student1.average()
