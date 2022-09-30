import PayrollDeductionClass as pd
import EmployeeClass as ec 

def net_pay(): 

    name = 'Jimmy Smith'
    idNumber_1 = 58475
    department = 'Information Systems'
    title = 'Developer'
    monthlysalary = 6800.00

    employee = ec.Employee(name,idNumber_1,department,title,monthlysalary)

    table = []

    table.append(pd.payroll('food court','8/14/2022',22.50,39119))
    table.append(pd.payroll('gift contribution','8/12/2022',25.00,58475))
    table.append(pd.payroll('food court','8/17/2022',15.25,21547))
    table.append(pd.payroll('vending machine','8/22/2022',3.00,58475))
    table.append(pd.payroll('vending machine','8/22/2022',2.75,58475))
       
    net_pay = employee.get_monthlysalary()
    
    for record in table:
        if record.get_empID() == employee.get_idNumber():
            net_pay = net_pay - record.get_charge()

    print('*** Employee Pay ***')
    print('Name:',employee.get_name())
    print('ID Number:',employee.get_idNumber())
    print('Department:',employee.get_department())
    print('Gross Pay:','$' + str(format(employee.get_monthlysalary(),',.2f')))
    print('Net Pay:','$' + str(format(net_pay,',.2f')))


net_pay()
