def get_income_tax(salary: float) -> float:
    p_allow = 11850
    taxable = salary - p_allow
    print("Taxable Income: ", taxable)

    if salary in range(0, 34501):
        return taxable * 0.2
    elif salary in range(34501, 150000):
        return taxable * 0.4
    else:
        return taxable * 0.45


print(get_income_tax(float(input("Enter Salary: "))))



