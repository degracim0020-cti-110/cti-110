# CTI - 110
# P5LAB
# Michaelangelo De Gracia
# 11/10/26

import random

def dispense_change(change) :

    # Converting the value to an integer
    change = round(change * 100)
    print(f"change owed as integer: $ {change}")

    # Determine how many dollars are needed
    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickles = change // 5
    change = change - (num_nickles * 5)

    num_pennies = change

    if num_dollars > 0:
        if num_dollars == 1:
            print(f"{num_dollars} Dollar")
        else:
            print(f"{num_dollars} Dollar")
    if num_quarters > 0:
        if num_quarters == 1:
            print(f"{num_quarters} quarters")
        else:
            print(f"{num_quarters} quarters")
    if num_dimes > 0:
        if num_dimes == 1:
            print(f"{num_dimes} dimes")
        else:
            print(f"{num_dimes} dimes")
    if num_nickles > 0:
        if num_nickles == 1:
            print(f"{num_nickles} nickles")
        else:
            print(f"{num_nickles} nickles")
    if num_pennies > 0:
        if num_pennies == 1:
            print(f"{num_pennies} pennies ")
        else:
            print(f"{num_pennies} pennies ")

def main():
    #Logic goes here 

    #Generate the amount owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"Amount owed: ${amount_owed:.2f}")

    #Create variable to represent money put into machine 
    money_in = float(input("How much cash will you put in the self-checkout machine?"))

    #Calculate the change owed to the customer
    change = money_in - amount_owed
    print(f"Change owed: ${change:.2f}")

    #Call the disperse_change function
    dispense_change(change)

#call the main function 
main()

