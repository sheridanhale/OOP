#EmployeeClass.py - Write a class named Employee that holds the following data about an employee in attributes: name, ID number, department, job title and monthly salary.The Employee class’s __init__ method should accept an argument for each attribute. The Employee class should have accessor methods for each attribute. All attribute should be hidden.

class Employee: 

    def __init__(self, name_1, idNumber_1, department_1, JobTitle_1, salary_1):
        self.__name = name_1
        self.__idNumber = idNumber_1
        self.__department = department_1
        self.__JobTitle = JobTitle_1
        self.__salary = salary_1

    def set_name(self, i_name):
        self.__name = i_name

    def set_idNumber(self,idNumber_1):
        self.__idNumber = idNumber_1
    
    def set_department(self,department_1):
        self.__department = department_1

    def set_JobTitle(self,JobTitle_1):
        self.__JobTitle = JobTitle_1
    
    def set_salary(self,salary_1):
        self.__salary = salary_1

    def get_name(self):
        return self.__name

    def get_idNumber(self):
        return self.__idNumber

    def get_department(self):
        return self.__department

    def get_JobTitle(self):
        return self.__JobTitle
    
    def get_salary(self):
        return self.__salary