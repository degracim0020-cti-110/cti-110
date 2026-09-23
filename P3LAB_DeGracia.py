# CTI - 11`0`
# P3lAB
# Michaelangelo De Gracia
# 9/23/26


# Get Value
change =float(input("Enter amount of money: $"))
print(f"Change amount: {change}")

#Convert the vaule into an integer 
change = int(change * 100)

print (f"change amount: {change}")

#Determine how many dollars are needed 
num_dollars = change // 100
change = change - (num_dollars * 100)

num_quarters = change // 25
change = change - (num_quarters * 25)

num_dimes = change // 10
change = change - (num_dimes * 10)