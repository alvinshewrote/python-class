# Get user inputs
basic_salary = float(input("Enter basic salary: "))
benefits = float(input("Enter benefits: "))

# Calculate gross salary
gross_salary = basic_salary + benefits
print(f"Gross Salary: {gross_salary}")

# Determine NHIF deduction based on Kenya NHIF rates
if gross_salary <= 5999:
    nhif = 150
elif gross_salary <= 7999:
    nhif = 300
elif gross_salary <= 11999:
    nhif = 400
elif gross_salary <= 14999:
    nhif = 500
elif gross_salary <= 19999:
    nhif = 600
elif gross_salary <= 24999:
    nhif = 750
elif gross_salary <= 29999:
    nhif = 850
elif gross_salary <= 34999:
    nhif = 900
elif gross_salary <= 39999:
    nhif = 950
elif gross_salary <= 44999:
    nhif = 1000
elif gross_salary <= 49999:
    nhif = 1100
elif gross_salary <= 59999:
    nhif = 1200
elif gross_salary <= 69999:
    nhif = 1300
elif gross_salary <= 79999:
    nhif = 1400
elif gross_salary <= 89999:
    nhif = 1500
elif gross_salary <= 99999:
    nhif = 1600
else:
    nhif = 1700

print(f"NHIF Deduction: {nhif}")


if gross_salary <= 18000:
    nssf = gross_salary * 0.06
else:
    nssf = 18000 * 0.06
    
print(f"NHIF Deduction: {nhif}")
print(f"NSSF Deduction: {nssf:.2f}")

nhdf = gross_salary * 0.015

print(f"NHDF Deduction: {nhdf:.2f}")

taxable_income = gross_salary - (nssf + nhdf + nhif)

print(f"\nTaxable Income: {taxable_income:.2f}")

if taxable_income <= 24000:
    paye = taxable_income * 0.10
elif taxable_income <= 32333:
    paye = (24000 * 0.10) + ((taxable_income - 24000) * 0.25)
else:
    paye = (24000 * 0.10) + (8333 * 0.25) + ((taxable_income - 32333) * 0.30)

personal_relief = 2400
paye = paye - personal_relief

if paye < 0:
    paye = 0

net_salary = gross_salary - (nhif + nssf + nhdf + paye)

print(f"PAYE (after relief): {paye:.2f}")
print(f"Net Salary: {net_salary:.2f}")


net_salary = gross_salary - (nhif + nhdf + nssf + paye)
print(f"\nNet Salary: {net_salary:.2f}")