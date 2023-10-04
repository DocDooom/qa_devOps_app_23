def get_income_tax(salary: float) -> float:
    p_allow = 11850
    taxable = salary - p_allow
    print("Taxable Income: ", taxable)
    tax = 0

    if salary in range(0, 34501):
        return round(taxable * 0.2, 2)
    elif salary in range(34501, 150000):
        tax +=(taxable - 34501) * 0.4
        tax += taxable * 0.2
        return round(tax, 2)
    else:
        tax += (taxable - 150000) * 0.45
        tax += (taxable - 34501) * 0.4


print(get_income_tax(float(input("Enter Salary: "))))



