# Michaelangelo De Gracia
# 9/10/26
# P1HW2
# Travel Expenses 

print("----Calculating your travel expenses----")
print("\n") # 2 newlines
# 3 numbers, start, sub_this
Travel_location = input ("Where are you traveling to?")
start = int(input("Enter your travel budget:"))
#print("you typed", start)
sub_this1 = int(input("How much will you spend on gas?: "))
sub_this2 = int(input("How much will you spend towards accomodation?: "))
sub_this3 = int(input("How much will you spend towards food?: "))
# Calculate the answer 
answer = start - sub_this1 - sub_this2 - sub_this3
# Print the answer
print()
print() # That gives 2 newlines, so would print("\n")
# Should look like: "10 - 4 - 2 is equal to 4"



print("----Travel Expenses Results----")
print("\n") # 2 new lines
print("Location:", Travel_location)
print("Budget:", start)
print("Gas:", sub_this1)
print("Accomodatons:", sub_this2)
print("Food:", sub_this3)

print("Leftover Balance:", answer)