# Michaelangelo De Gracia
# 9/16/26
# P2HW1
# Nicely Formated Travel Expenses 

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



print("------Travel Expenses Results------")
print("\n") # 2 new lines
print(f"{'Location:':<17} {Travel_location}")
print(f"{'Budget:':<17} ${start: .2f}")
print(f"{'Gas:':<17} ${sub_this1: .2f}")
print(f"{'Accommodation:':<17} ${sub_this2: .2f}")
print(f"{'Food:':<17} ${sub_this3: .2f}")
print("------------------------------------")
print(f"{'Leftover Balance:':<15} ${answer: .2f}")