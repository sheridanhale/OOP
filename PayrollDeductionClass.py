class payroll:

    def __init__(self,description_1,date_1,chrg_1,id_1):
        self.__description = description_1 
        self.__date = date_1 
        self.__chrg = chrg_1 
        self.__empID = id_1  

    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date

    def get_chrg(self):
        return self.__chrg

    def get_empID(self):
        return self.__empID