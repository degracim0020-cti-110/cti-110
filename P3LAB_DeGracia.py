# CTI - 11`0`
# P3lAB
# Michaelangelo De Gracia
# 9/23/26


# Get Value
change =float(input("Enter amount of money: $"))

print(f"Change amount: {change}")

# Convert the vaule into an integer 

change = round(change * 100)

print (f"change amount: {change}")

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
        print(f"{num_pennies} penny")
    else:
        print(f"{num_pennies} penny")