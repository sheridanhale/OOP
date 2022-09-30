class Employee: 

    def __init__(self, name_1, id_1, department_1, job_1, salary_1):
        self.__name = name_1
        self.__id = id_1
        self.__department = department_1
        self.__job = job_1
        self.__salary = salary_1

    def set_name(self, i_name):
        self.__name = i_name

    def set_id(self,id_1):
        self.__id = id_1
    
    def set_department(self,department_1):
        self.__department = department_1

    def set_job(self,job_1):
        self.__job = job_1
    
    def set_salary(self,salary_1):
        self.__salary = salary_1

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_department(self):
        return self.__department

    def get_job(self):
        return self.__job
    
    def get_salary(self):
        return self.__salary