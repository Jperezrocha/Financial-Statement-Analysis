# Compound interest
def compound_interest():
    PV = float(input('Whats is the present value? '))
    r = float(input('What is the growth rate? '))
    n = float(input('Number of times interest is compounded?  '))
    t = float(input('time periods in years? '))
    return PV * (1 + r / n) ** (n * t)


print(round(compound_interest()))


# Present Value
def present_value():
    FV = float(input('What is the Future Value? '))
    r = float(input("What is the Discount rate? "))
    n = float(input('Time period in years? '))
    return FV / (1 + r) ** n


print(round(present_value))

#Net Present Value
def net_PV():
