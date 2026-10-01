# Michaelangelo De Gracia
# 10/1/26
# P3HW1
# This program takes a number grade , determines average and displays letter grade for average.




# Enter grades for six modules

mod_1 = float(input("Enter grade for Module 1: "))
mod_2 = float(input("Enter grade for Module 2: "))
mod_3 = float(input("Enter grade for Module 3: "))
mod_4 = float(input("Enter grade for Module 4: "))
mod_5 = float(input("Enter grade for Module 5: "))
mod_6 = float(input("Enter grade for Module 6: "))

# add grades entered to a list

Grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

Lowest_Grade = min(Grades)
Highest_Grade = max(Grades)
Sum = sum(Grades)
count = len(Grades)

Average_grade = sum(Grades) / len(Grades)

# determine letter grade for average

if Average_grade >= 90:
    letter_grade = 'A'
elif Average_grade >= 80:
    letter_grade = 'B'
elif Average_grade >= 70:
    letter_grade = 'C'
elif Average_grade >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'
print("---------Results---------")
print(f'Lowest Grade: {Lowest_Grade}')
print(f'Highest Grade: {Highest_Grade}')
print(f'Sum of Grades: {Sum}')
print(f'Average Grade: {Average_grade:.2f}')
print("-------------------------")
print(f'Your grade is: {letter_grade}')






