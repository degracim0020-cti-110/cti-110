# De Gracia
# 10/11/2026
# Salary Calculator with loops

# Request employee info
name = input("Enter employee's name or 'done' to finish: ")

# Create Accumulator variables for overtime pay, regular pay, and gross pay, and employee count
overtime_pay_total = 0
regular_pay_total = 0
gross_pay_total = 0
employee_count = 0

while name != 'done':
    #add employee count plus one
    employee_count += 1
    #ask for hours and rate
    hours = float(input("How many hours did " +name+ " work this week? "))
    rate = float(input("What is " +name+ "'s hourly pay? "))


    #Evaluate overtime
    if hours > 40:
        # calculate overtime
        overtime_hours = hours - 40
        # calculate over pay
        overtime_pay = overtime_hours * (rate * 1.5)
        # Calculate salary for regular hours 
        regular_pay = 40 * rate
        # Calcualte Gross pay
        gross_pay = regular_pay + overtime_pay
    else:
        overtime_pay = 0
        overtime_hours = 0
        regular_pay = hours * rate
        gross_pay = regular_pay
    
    # Add to accumulator variables
    overtime_pay_total += overtime_pay
    regular_pay_total += regular_pay
    gross_pay_total += gross_pay


    # Display results
    print("-----------------------------")
    print("Employee Name:", name)
    print(f'{"Hours Worked" :<15}{"Pay Rate":<12}{"Overtime Pay":<15}{"Regular Pay":<15}{"Gross Pay":<15}')
    print("----------------------------------------------------------")
    print(f'{hours:<15.2f}{rate:<12.2f}{overtime_pay:<15.2f}{regular_pay:<15.2f}{gross_pay:<15.2f}')

    name = input("Enter employee's name or 'done' to finish: ")

print("Total number of employees processed:", employee_count)
print("Total amount paid for overtime: $", format(overtime_pay_total, '.2f'))
print("Total amount paid for regular pay: $", format(regular_pay_total, '.2f'))
print("Total amount paid for gross pay: $", format(gross_pay_total, '.2f'))