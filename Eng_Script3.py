# William Eng
# weng2@oakland.edu
#  We will simulate a simple online shopping website

products = [["PlayStation5 Console", 499.99],["Xbox Console", 349.99],["Nintendo Switch",299.99],["AMD Radeon 7900XTX",1100.99],["Nvidia Geforce 4080", 1199.99]]
    
print("----- Product List (ID, Product, Price) -----")
for i in range(len(products)):
    print("Product ID: {}\t Product Name: {}\t Product Price: {}".format((i+1),products[i][0],products[i][1]))
print()
shoppingList=[]
userChoice = 0
userChoice = input("Input desired product ID or press q to exit: ")
while userChoice != 'q':
    try:
        userChoice = int(userChoice)
        if userChoice <= 0 or userChoice > len(products):
            print("Invalid input.  Item does not exist. Input desired product ID or press q to exit: ")
        else:
            shoppingList.append(products[userChoice]) 
    except ValueError:
        print("Invalid input.  Input desired product ID or press q to exit: ")
    userChoice = input("Input desired product ID or press q to exit: ")
print()
print("----- Your Shopping List (ID, Product, Price) -----")
totalList = 0
for i in range(len(shoppingList)):
    print("Product ID: {}\t Product Name: {}\t Product Price: {}".format((i+1),shoppingList[i][0],shoppingList[i][1]))
    totalList += shoppingList[i][1]
print("-----------------------------------------------------------------")
print("There are {} items".format(len(shoppingList)))
print("The total is ${}".format(round(totalList,2)))

# Test case
# 1
# 2
# 3
# 4

# -1 invalid
# a invalid
# 7 invalid
# 0 invalid

# q 0
