bill = input('How much is the bill before sales tax and tip?')
tax = input('How much is the sales tax rate for your order?')
bill_tax = bill + (bill * tax)
tip = input('How much would you like to include for your order?')
bill_tax_tip = bill_tax + (bill_tax * tip)
total = bill_tax_tip
share = input('How many individuals will be spliting the bill?')

print(bill)
print(tax)
print(tip)
print(share)
print(bill_tax)
print(total)
