
"""
Algorithm:
1. Define fixed salary values, hourly wage, overtime rate, and tax rate.
2. Get employee details and work hours, then generate a random employee ID.
3. Calculate work experience, overtime pay, leave deduction, gross salary, bonus, and tax.
4. Calculate net salary before bonus, daily net salary, and final payable salary.
5. Determine employee experience, income, and loyalty statuses.
6. Print employee information, employment status, and salary details.



Example Input:
Employee Full Name: Mohyaldin Amiri
Employee Department: Programmer
Employee Overtime Hours: 50
Leave Hours: 16
Employment Year: 2016



Example Output:
----------INFO----------
Employee Name: Mohyaldin Amiri      Department: Programmer      Employee ID: PRMOH1643
Monthly Base Salary: 21000000    Daily Base Salary: 700000    Hourly Base Salary: 87500    Overtime Hourly Rate: 122499
Tax Rate: 9%       Tax Amount:2441245
----------Status----------
Current Year: 2026      Employment Year: 2016      Work Experience: 10 Year
Leave Hours: 16      Overtime Hours: 50      Salary Deduction For Leave: 0
Employee Experience Status: Experienced     Employee Loyalty Status: Loyal      Employee Income Status: High Income
----------Salary----------
Payable Net Salary: 29683705      Daily Net Salary No Bonus: 822790
Bonus Amount: 5000000      Overtime Salary: 6124950
"""


import random
from datetime import datetime


#Start - Fixed Values
MonthlyBaseSalary = int(21000000)
HourlyWage = int(MonthlyBaseSalary / 30 / 8)
OvertimeHourlyRate = int(HourlyWage * 1.4)
TaxRate = int(9)
#End - Fixed Values
#Start - User Inputs
FullName = input("Employee Full Name: ").strip().title()
Department = input("Employee Department: ").strip().title()
OvertimeHours = int(input("Employee Overtime Hours: "))
LeaveHours = int(input("Leave Hours: "))
EmploymentYear = int(input("Employment Year: "))
#End - User Inputs

#Start - Generating Employee ID
EmployeeID = f'{Department[:2].upper()}{FullName[:3].upper()}{str(EmploymentYear)[-2:]}{random.randint(1, 100)}'
#End - Generating Employee ID

#Start - Salary Calculations
WorkExperience = datetime.now().year - EmploymentYear
OvertimeSalary = OvertimeHourlyRate * OvertimeHours
SalaryDeductionForLeave = 0 if LeaveHours <= 16 else (LeaveHours - 16) * HourlyWage
GrossSalary = int(MonthlyBaseSalary + OvertimeSalary)
BonusAmount = 5000000 if WorkExperience >= 5 else 0
TaxAmount = int(GrossSalary * TaxRate / 100)

MonthlyNetSalary = GrossSalary - TaxAmount 
MonthlyNetSalary -= SalaryDeductionForLeave
DailyNetSalary = int(MonthlyNetSalary / 30)
MonthlyNetSalary += BonusAmount #Payable Salary
#End - Salary Calculations



#Start - Employee Status
EmployeeExperience = "Experienced" if WorkExperience >= 5 else "Less Experienced"
EmployeeIncome = "High Income" if  MonthlyNetSalary >= 25000000 else "Low Income"
EmployeeLoyalty = "Loyal" if WorkExperience >= 5 and OvertimeHours >= 20 else "Normal"
#End - Employee Status


#ُStart - Output
print("----------INFO----------")
print(f'Employee Name: {FullName}      Department: {Department}      Employee ID: {EmployeeID}')
print(f'Monthly Base Salary: {MonthlyBaseSalary}    Daily Base Salary: {int(MonthlyBaseSalary / 30)}    Hourly Base Salary: {int((MonthlyBaseSalary / 30) / 8)}    Overtime Hourly Rate: {OvertimeHourlyRate}')
print(f'Tax Rate: {TaxRate}%       Tax Amount:{TaxAmount}')

print("----------Status----------")
print(f'Current Year: {datetime.now().year}      Employment Year: {EmploymentYear}      Work Experience: {WorkExperience} Year')
print(f'Leave Hours: {LeaveHours}      Overtime Hours: {OvertimeHours}      Salary Deduction For Leave: {SalaryDeductionForLeave}')

print(f'Employee Experience Status: {EmployeeExperience}     Employee Loyalty Status: {EmployeeLoyalty}      Employee Income Status: {EmployeeIncome}')

print("----------Salary----------")
print(f'Payable Net Salary: {MonthlyNetSalary}      Daily Net Salary No Bonus: {DailyNetSalary}')
print(f"Bonus Amount: {BonusAmount}      Overtime Salary: {OvertimeSalary}")
#ُEnd - Output