class Employee:
    start_time="10 A.M"
    end_time="6 P.M"
    def change_time(self,newend_time):
        self.end_time=newend_time
class Teacher(Employee):
    def __init__(self,subject):
        self.subject=subject
class AdminStaff(Employee):
    def __init__(self,role):
        self.role=role
staff1=AdminStaff("Manager")
t1=Teacher("maths")
t1.change_time("1 P.M")
print(t1.start_time)
print(t1.end_time)
print(t1.subject)
print(staff1.start_time)
print(staff1.end_time)
print(staff1.role)
