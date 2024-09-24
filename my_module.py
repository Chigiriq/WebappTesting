

def max3(i, j, k):
    if (i > j):
        if (i > k):
            return i
        else:
            return k
    else:
        if (j > k):
            return j
        else:
            return k
        

def odd(i, j , k):
    oddAmount = (i + j + k) % 2
    if (oddAmount == 1):
        return True
    else:
        return False

def majority(i, j, k):
    if ((i == j and i == True) or (j == k and j ==True) or (i == k and k == True)):
        return True
    else:
        return False

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return "Name: " + self.name + ", Salary: " +str(self.salary)

class Manager(Employee): #make this a child of employee
    def __init__(self, name, salary, dept):
        super().__init__(name, salary)
        self.dept = dept

    def get_details(self):
        return "Name: " + self.name + ", Salary: " + str(self.salary) + ", Department: " + self.dept