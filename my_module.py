

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
    if ((i == j and i == True) and j == k):
        return True
    else:
        if ((i == j and i == True) or (i == k and i == True) or (j == k and j == True)): #ij or ik or jk
            return False
        else: 
            return True

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
        return "Name: " + self.name + ", Salary:", self.salary

class Manager: #make this a child of employee
    def __init__(self, name, salary, dept):
        self.name = name
        self.salary = salary
        self.dept = dept

    def get_details(self):
        return "Name: " + self.name + ", Salary:", self.salary + ", Department: " + self.dept