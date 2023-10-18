# William Eng
# weng2@oakland.edu
# prompts the user for their amount of money, then reports how many Nintendo Switches the person can afford, and how much more money they will need to afford an additional Switch

# set price for switch
priceSwitch = 299.99

# ask user for money
money = input("How much amount of money do you have? ")
# try to convert to float if it's a number
try:
    money = float(money)
    # if it's a negative number, need to balnce and add cost of switch
    if money <= 0:
        numSwitch = 0
        remSwitch = round(abs(money) + priceSwitch,2)
    # if it's a positive number, see how many whole switches can be bought and how much more for is needed for additional switch
    else:
        numSwitch = int(money // priceSwitch)
        remSwitch = round(priceSwitch - (money % priceSwitch),2)
    # round money to 2 decimal places afterwards avoid potential rounding issues
    money = round(money,2)
    # need to format, other wise the round could return .0 instead of .00
    print("With ${:.2f} amount of money, you can buy {} Nintendo Switch(es), you can afford one more Switch if you have ${} more".format(money,numSwitch,remSwitch))
    # if it is not a number, then tell user to enter numbers only
except ValueError:
    print("Invalid input.  Please provide numbers only")

# Test Input
# 500.00000
# -3999
# asdf