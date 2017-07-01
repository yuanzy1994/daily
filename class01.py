class Employee:
    'Something for employee ...'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.age = 20
        self.sex = 'N'
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name:", self.name,  ",Salary:", self.salary


emp1 = Employee("yuanzy", 3000)
emp2 = Employee("shenjc", 1000)

emp1.age = 18
print emp1.age

del emp1.age

emp2.sex = "M"

emp1.displayEmployee()
emp2.displayEmployee()

# emp1.displayCount()
emp2.displayCount()

if hasattr(emp1, 'age'):
    print "Yes"
else:
    print "No"

get_value = getattr(emp2, 'sex')
print get_value

# else method
'''
getattr(self,method)
hasattr(self,method)
setattr(self,method)
delattr(self,method)
'''

print "Employee.__doc__:", Employee.__doc__
print "Employee.__module__:", Employee.__module__
