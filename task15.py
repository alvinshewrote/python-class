def get_basic_salary():
    basic_salary = float(input("Enter basic salary: "))
    return basic_salary

def get_benefits():
    benefits = float(input("Enter benefits: "))
    return benefits

def calculate_gross_salary(basic_salary, benefits):
    return basic_salary + benefits

def calculate_nhif(gross_salary):
    if gross_salary <= 5999:
        return 150
    elif gross_salary <= 7999:
        return 300
    elif gross_salary <= 11999:
        return 400
    elif gross_salary <= 14999:
        return 500
    elif gross_salary <= 19999:
        return 600
    elif gross_salary <= 24999:
        return 750
    elif gross_salary <= 29999:
        return 850
    elif gross_salary <= 34999:
        return 900
    elif gross_salary <= 39999:
        return 950
    elif gross_salary <= 44999:
        return 1000
    elif gross_salary <= 49999:
        return 1100
    elif gross_salary <= 59999:
        return 1200
    elif gross_salary <= 69999:
        return 1300
    elif gross_salary <= 79999:
        return 1400
    elif gross_salary <= 89999:
        return 1500
    elif gross_salary <= 99999:
        return 1600
    else:
        return 1700


def calculate_nssf(gross_salary):
    if gross_salary <= 18000:
        return gross_salary * 0.06
    else:
        return 18000 * 0.06


def calculate_nhdf(gross_salary):
    return gross_salary * 0.015

def calculate_paye(taxable_income):
    if taxable_income <= 24000:
        paye = taxable_income * 0.10
    elif taxable_income <= 32333:
        paye = (24000 * 0.10) + ((taxable_income - 24000) * 0.25)
    else:
        paye = (24000 * 0.10) + (8333 * 0.25) + ((taxable_income - 32333) * 0.30)

    personal_relief = 2400
    paye -= personal_relief
    return max(paye, 0)  


def calculate_net_salary(basic_salary, benefits):
    gross_salary = calculate_gross_salary(basic_salary, benefits)
    nhif = calculate_nhif(gross_salary)
    nssf = calculate_nssf(gross_salary)
    nhdf = calculate_nhdf(gross_salary)

    taxable_income = gross_salary - (nssf + nhdf + nhif)
    paye = calculate_paye(taxable_income)
    net_salary = gross_salary - (nhif + nssf + nhdf + paye)

    print(f"\nGross Salary: {gross_salary:.2f}")
    print(f"NHIF Deduction: {nhif}")
    print(f"NSSF Deduction: {nssf:.2f}")
    print(f"NHDF Deduction: {nhdf:.2f}")
    print(f"Taxable Income: {taxable_income:.2f}")
    print(f"PAYE (after relief): {paye:.2f}")
    print(f"Net Salary: {net_salary:.2f}")

    return net_salary

basic_salary = get_basic_salary()
benefits = get_benefits()

calculate_net_salary(basic_salary, benefits)