"""THIS IS THE SIMPLE EXAMPLE OF OVERRIDING METHODS IN PYTHON"""

class Employee:
    def __init__(self,nm,sly):
        self.name=nm;
        self.salary=sly;
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary
class SalesOfficer(Employee):
    def __init__(self,nm,sly,inc):
        super().__init__(nm,sly)
        self.incnt=inc
    def getSalary(self):
        return self.salary+self.incnt

e=Employee("Rajesh",9000)
print('Total Salary for {} is Rs.{}'.format(e.getName(),e.getSalary()))
s1=SalesOfficer('Teja',100000,1000)
print('Total Salary of {} id Rs. {}'.format(s1.getName(),s1.getSalary()))


