import auto_shop as A

def main():
    print('Enter the following customer data: ')
    name = input('Name: ')
    address = input('Address: ')
    phone = float(input('Phone Number: '))
    print('---')

    customer = A.Customer(name, address, phone)


    print('Enter the following car data: ')
    make = input('Make: ')
    model = input('Model: ')
    year = float(input('Year: '))
    print('---')
    
    car = A.Car(make, model, year)


    print('Enter the following service quote data: ')
    pcharge = float(input('Parts Charge: $'))
    lcharge = float(input('Labor Charge: $'))
    print('---')

    servicequote = A.ServiceQuote(pcharge, lcharge)
    tax_rate = 0.20
    sales_tax = pcharge * tax_rate
    total_charges = pcharge + lcharge + \
        (pcharge * tax_rate)
    print('Your sales tax is: $', sales_tax)
    print('Your total charges are: $', total_charges)

main()