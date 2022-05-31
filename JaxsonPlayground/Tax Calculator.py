
Salary = int(input("Enter your salary: "))
SalaryAfter = Salary
#TODO: change hardcoded percentages with real percentages

#IE tax amount
IEtax = Salary * 0.0158
if IEtax > 952.74:
    IEtax = 952.74
print("IEtax (AEtax) =", IEtax)

#CPP tax amount
CPPtax = Salary * 0.057
if CPPtax > 3499.8:
    CPPtax = 3499.8
print("CPPtax (RCPtax) =", CPPtax)

#Federal tax amount

FedTax = 0
while SalaryAfter > 0:
    if(SalaryAfter > 50197):
        FedTax += 50197 * 0.15
        SalaryAfter -= 50197
    else:
        FedTax += SalaryAfter * 0.15
        SalaryAfter -= SalaryAfter
        break

    if(SalaryAfter > 50197):
        FedTax += 50197 * 0.205
        SalaryAfter -= 50197
    else:
        FedTax += SalaryAfter * 0.205
        SalaryAfter -= SalaryAfter
        break

    if(SalaryAfter > 55233):
        FedTax += 55233 * 0.26
        SalaryAfter -= 55233
    else:
        FedTax += SalaryAfter * 0.26
        SalaryAfter -= SalaryAfter
        break

    if(SalaryAfter > 66083):
        FedTax += 66083 * 0.29
        SalaryAfter -= 66083
    else:
        FedTax += SalaryAfter * 0.29
        SalaryAfter -= SalaryAfter
        break

    FedTax += SalaryAfter * 0.33
    SalaryAfter -= SalaryAfter
print("Federal tax =", FedTax)

#Provincial Tax
ProvTax = 0
SalaryAfter = Salary
while SalaryAfter > 0:
    if(SalaryAfter > 29590):
        ProvTax += 29590 * 0.0879
        SalaryAfter -= 29590
    else:
        ProvTax += SalaryAfter * 0.0879
        SalaryAfter -= SalaryAfter
        break

    if(SalaryAfter > 29590):
        ProvTax += 29590 * 0.1495
        SalaryAfter -= 29590
    else:
        ProvTax += SalaryAfter * 0.1495
        SalaryAfter -= SalaryAfter
        break

    if(SalaryAfter > 33820):
        ProvTax += 33820 * 0.1667
        SalaryAfter -= 33820
    else:
        ProvTax += SalaryAfter * 0.1667
        SalaryAfter -= SalaryAfter
        break

    if(SalaryAfter > 57000):
        ProvTax += 57000 * 0.175
        SalaryAfter -= 57000
    else:
        ProvTax += SalaryAfter * 0.175
        SalaryAfter -= SalaryAfter
        break

    ProvTax += SalaryAfter * 0.21
    SalaryAfter -= SalaryAfter
print("Provincial tax =", ProvTax)


print("TOTAL  Deductions =", IEtax + CPPtax + FedTax + ProvTax)

print("Net Salary =", Salary - (IEtax + CPPtax + FedTax + ProvTax))