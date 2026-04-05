class student :
    schoolname = "ABC school"

    def __init__(self,name,course):
        # print(" Whenever a new object is created I am called automaticaly")
        # print(self)
        self.name=name
        self.course=course


student1=student("subh","Btech") # init method will be called 
print("Student 1 name",student1)
print("Stident 1 cource == ", student1.course)


student2=student("Ankit","bsc")
print("Student 2 name",student2)
print("Stident 2 cource == ", student2.course)
