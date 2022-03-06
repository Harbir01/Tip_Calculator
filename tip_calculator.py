# Capture User inputs in functions
# This function is capturing the user input for bill
def get_bill():
    # Initalize while loop condition
    is_float = False
    # Loop until correct input
    while is_float == False:
        bill = input('\nHow much is the bill before sales tax and tip? ')
        # Test if input is float and greater than 0
        try:
            if float(bill) <= 0:   # Input is convertible to float but zero or less
                print("Zero or negative bill is not calculable. Please try again.")
            else:       # Input passes test
                is_float = True     # No errors so while loop conditon met
        except ValueError:      # Input isn't convertible to float
            print('The input you entered is not valid. Please try again.')
    print(f'The bill before taxes and tip is ${bill}.')
    return float(bill)      #return users absolute float input

# Function captures user input for tax
def get_tax():
    is_float = False
    while is_float == False:
        tax = input('\nHow much percent is the sales tax rate for your order? ')
        try:
            if float(tax) < 0:
                print('Negative tax is not possible. Please try again.')
            else:
                is_float = True
        except ValueError:
            print('The input you entered is not valid. Please try again.')
    print(f'The tax amount entered is {tax}%.')
    return float(tax) / 100

# Function captures user input for tip
def get_tip():
    is_float = False
    while is_float == False:
        tip = input('\nHow much percent tip would you like to include for your order? ')
        try:
            if float(tip) <= 0:
                print('Zero or negative tip is not allowed. Please try again.')
            else:
                is_float = True
        except ValueError:
            print('The input you entered is not valid. Please try again.')
    print(f'The tip amount entered is {tip}%.')
    return float(tip) / 100

# Function captures user input for share
def get_share():
    is_int = False
    while is_int == False:
        share = input('\nHow many individuals will be spliting the bill? ')
        try:
            if int(share) < 1:
                print('At least one person must be paying. Please try again.')
            else:
                is_int = True
        except ValueError:
            print('The input you entered is not valid. Please try again.')
    print(f'Okay, The bill is being split {share} ways.')
    return int(share)

# Calculations
def calculate_total_bill():
    bill = get_bill()
    tax = get_tax()
    tip = get_tip()
    share = get_share()

    total_tax = bill * tax
    total_tip = bill * tip
    total_bill = bill + bill * tax + bill * tip
    share_amount = total_bill / share

    print(f'The total tax amount for the order is ${round(total_tax, 2)}.')
    print(f'The total tip amount for the order is ${round(total_tip, 2)}.')
    print(f'The total bill including tax and tip is ${round(total_bill, 2)}.')
    print(f'Each person should pay ${round(share_amount, 2)}.')

print('\nHello There, Welcome to the Tip Calculator. \nThis tool will help you calculate your tip amounts. \nAllowing you to show your appreciation to the service providers you utilize.\n')

is_again = True
while is_again:
    calculate_total_bill()
    run_again = input('Would you like to calculate another bill? (y/n) ')
    if run_again[0:1].lower() == 'n':
        is_again = False

print('Thank you for using the Tip Calculator. Bye.')