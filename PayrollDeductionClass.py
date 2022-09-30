#PayrollDeductionClass.py - Write a class that represents a payroll deduction transaction. Each instance should have the description, date, charge amount and employee ID as attributes. The class’s __init__ method should accept an argument for each attribute. The class should have accessor methods for each attribute. All attribute should be hidden.
class payroll:

    def __init__(self,description_1,date_1,charge_1,empID_1):
        self.__description = description_1 
        self.__date = date_1 
        self.__charge = charge_1 
        self.__empID = empID_1  

    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date

    def get_charge(self):
        return self.__charge

    def get_empID(self):
        return self.__empID