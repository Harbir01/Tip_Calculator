# Capture User inputs in functions
# This function is capturing the users input for bill
def get_bill():
    is_float = False        #Initalize Condition
    while is_float == False:         #While loop with condition
        bill = input('\nHow much is the bill before sales tax and tip?')      #User Input  
        try:                  
                float_bill = abs((float(bill)))        #Turns input into absolute float    
                is_float = True                       #No errors so while loop conditon met
        except:                                     #If error exception will be printed
                print('The input you entered is not valid, please try again.')
    return float_bill                                    #return users absolute float input

# Function captures user input for tax 
def get_tax():
    is_float = False
    while is_float == False:
        tax = input('\nHow much percent is the sales tax rate for your order?')
        try:
            float_tax = abs(float(tax))/100
            is_float = True
        except:
            print('The input you entered is not valid, please try again.')
    return float_tax

#Function captures user input for tip
def get_tip():
    is_float = False
    while is_float == False:
        tip = input('\nHow much percent tip would you like to include for your order?')
        try:
            float_tip = abs(float(tip))/100
            is_float = True
        except:
            print('The input you entered is not valid, please try again.')
    return float_tip

# Function captures user input for share
def get_share():
    is_int = False
    while is_int == False:
        share = input('\nHow many individuals will be spliting the bill?')
        try:
            int_share = abs(int(share))
            is_int = True
        except:
            print('The input you entered is not valid, please try again.')
    return int_share

# Calculations
#Function accepts bill, tax, tip and generates total bill
def get_bill_total(bill,tax,tip):
    bill_total = bill + bill*tax + bill*tip
    return bill_total

#Function accepts bill total and divides it by number of shares
def get_per_cal(bill_total,share):
    per_cal = bill_total/share
    return per_cal
        


print('\nHello There, Welcome to the Tip Calculator. \nThis tool will help you calculate your tip amounts. \nAllowing you to show your appreciation to the service providers you utilize.\n')

print('Please be sure to use positive numbers, \nif you do decide to use negative numbers \nthey will be treated as positive number.\n')

# #Print Calculations
#Storing functions into variables and printing for user
bill = get_bill()
print(f'The bill before taxes and tip is ${bill}.')
tax = get_tax()
print(f'The tax amount entered is {tax*100}%.')
tip = get_tip()
print(f'The tip amount entered is {tip*100}%.')
share = get_share()
print(f'Okay, The bill is being split {share} ways.')

print(f'\nThe tax amount is ${bill*tax:.2f}.')
print(f'The tip amount is ${bill*tip:.2f}.')
bill_total = get_bill_total(bill,tax,tip)
print(f'The total bill including tax and tip is ${bill_total:.2f}')
per_bill = get_per_cal(bill_total, share)
print(f'Each person should pay ${per_bill:.2f}')


