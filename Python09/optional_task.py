# calculate monthly wage for 2 employees
# employee can be salesperson or manager
# salesperson can earn 8% commission on gross sales also
# add to the fixed salary R2000 per/m
# manager earn a hourly rate of R40


employee_position = input("Please type in the position of the employee of concern: (manager / salesperson) ")
print(employee_position)

if employee_position == "salesperson":
    gross_sales = int(input("Please type in the gross sales for salesperson: R"))
   

else: 
    hours_worked = int(input("Please type in the hours worked by the manager: "))


# assuming hours worked weekly 8 hours daily x 5 days = 40 hours per week, 40*4 = 160 per month
if employee_position == "manager":
    monthly_wage = 40 * hours_worked
else:
    monthly_wage = 2000 + 0.08 * gross_sales
    
total_monthly_wage = print(f"The total monthly wage for this employee is: R{monthly_wage}")