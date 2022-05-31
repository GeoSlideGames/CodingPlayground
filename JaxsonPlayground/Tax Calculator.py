
Salary = int(input("Enter your salary: "))
SalaryAfter = int(Salary)
#TODO: change hardcoded percentages with real percentages

#IE tax amount
IEtax = Salary * 0.05
if IEtax > 30000:
    IEtax = 30000
print(IEtax)

#CPP tax amount
CPPtax = Salary * 0.08
if CPPtax > 40000:
    CPPtax = 40000
print(CPPtax)

#Federal tax amount

FedTax = 0
while SalaryAfter > 0:
    if(SalaryAfter > 50000):
        FedTax += 50000 * 0.15
        SalaryAfter -= 50000
    else:
        FedTax += SalaryAfter * 0.15
        SalaryAfter -= SalaryAfter
        break

    if(SalaryAfter > 40000):
        FedTax += 40000 * 0.205
        SalaryAfter -= 40000
    else:
        FedTax += SalaryAfter * 0.205
        SalaryAfter -= SalaryAfter
        break

    if(SalaryAfter > 30000):
        FedTax += 30000 * 0.26
        SalaryAfter -= 30000
    else:
        FedTax += SalaryAfter * 0.26
        SalaryAfter -= SalaryAfter
        break

    if(SalaryAfter > 30000):
        FedTax += 30000 * 0.29
        SalaryAfter -= 30000
    else:
        FedTax += SalaryAfter * 0.29
        SalaryAfter -= SalaryAfter
        break

    FedTax += SalaryAfter * 0.33
    SalaryAfter -= SalaryAfter
print(FedTax)