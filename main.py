# Compound interest
def compound_interest():
    PV = float(input('What is the present value? '))
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


# Net Present Value
def NPV():
    INV = float(input('Amount of Initial Investment? '))
    CF1 = float(input("Cash Flow 1? "))
    CF2 = float(input('Cash Flow 2? '))
    CF3 = float(input('Cash Flow 3? '))
    r = float(input('What is the discount rate? '))
    return INV + (CF1 / (1 + r) ** 1) + (CF2 / (1 + r) ** 2) + (CF3 / (1 + r) ** 3)


print(round(NPV()))


# Capital Asset Pricing Model
def CAPM():
    r = float(input('What is the expected return?'))
    rf = float(input('What is the risk-free rate?'))
    B = float(input('Whats is the stock beta? '))
    rm = float(input('Whats is the expected return of the market? '))
    return rf + B * (rm - rf)


print(round(CAPM()))


# Black Scholes Option Pricing Model

def OPM():
    S = float(input("What is the Stock price? "))
    X = float(input("The exercise price"))
    r = float(input("What is the risk-free interest rate? "))
    t = float(input("Time to Maturity? "))
    Nd1 = float(input("Normal distribution"))
    Nd2 = float(input("Normal distribution"))
    return S * Nd1 - X ** (-r * t) * Nd2


print(OPM())


# Debt to equity ratio
def Deb_to_equity():
    total_debt = float(input("What is the total debt? "))
    total_equity = float(input("What is the total equity? "))
    return total_debt / total_equity


print(Deb_to_equity())


# Return on Investment
def ROI():
    gain_fromINV = float(input("Gain from Investment? "))
    cost_of_INV = float(input("Cost of Investment? "))
    return (gain_fromINV - cost_of_INV) / cost_of_INV


print(ROI())


# Price to Earnings Ratio
def PE_ratio():
    stock_price = float(input("Current Stock Price? "))
    eps = float(input("Earnings per Share? "))
    return stock_price / eps


print(PE_ratio())


# Dividend Yield
def DY():
    ADPS = float(input("What is the annual dividend per share? "))
    SP = float(input("What is the stock price? "))
    return ADPS / SP


print(DY())
