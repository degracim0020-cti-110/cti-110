# CTI 110
# p2HW2 - List Basics
# Michaelangelo De Gracia
# Aggregate test scores with built-in functions

# Input grades
grade1 = float(input("Enter grade 1: "))
grade2 = float(input("Enter grade 2: "))
grade3 = float(input("Enter grade 3: "))
grade4 = float(input("Enter grade 4: "))
grade5 = float(input("Enter grade 5: "))
grade6 = float(input("Enter grade 6: "))

# Put grades in a list
grade_list = [grade1, grade2, grade3, grade4, grade5, grade6]

# Calculate average
min_grade = min(grade_list)
max_grade = max(grade_list)
total     = sum(grade_list)
count     = len(grade_list)
# Calculate average continued 
average_grade = sum(grade_list) / len(grade_list)

# Display output
print("--------Results--------")
print(f"{'Lowest Grade:':<18}{min_grade}")
print(f"{'Highest Grade:':<18}{max_grade}")
print(f"{'Sum of Grades:':<18}{total}")
print(f"{'Average:':<18}{average_grade:.2f}")
print("-----------------------")