def credit_balance(balance, annualInterestRate, min_pay_rate, month):
    '''
    this is a recursive function for calculating your credit balance
    after x months
    '''
    
    if month <= 0:
        return balance
    else:
        min_payment = (balance * min_pay_rate)
        print(min_payment)
        unpaid_balance = balance - min_payment
        interest = (annualInterestRate/12.0)*(unpaid_balance)
        new_balance = unpaid_balance + interest
        month = month - 1
        return credit_balance(new_balance, annualInterestRate, min_pay_rate, month)

#print credit_balance(5000, 0.18, 0.02, 12)

def fixed_payment_calc(balance, annualInterestRate, min_payment, month):
    '''
    this function returns the balance after you've paid a flat fee each 
    month for x number of months...

    where x is the argument of the fixed_payment_calc fuction, "month"...
    sorry, this is baby's first script, bad variable names are inevitable
    '''

    if month <= 0:
        return balance
    else:
        unpaid_balance = balance - min_payment
        interest = (annualInterestRate/12.0)*(unpaid_balance)
        new_balance = unpaid_balance + interest
        month = month - 1
        return fixed_payment_calc(new_balance, annualInterestRate, min_payment, month)


print(fixed_payment_calc(5000, 0.18, 451.626022, 12))
print(fixed_payment_calc(5000, 0.18, 0, 12))

def min_payment_calculator(balance, annualInterestRate, min_payment, month):
    '''
    this is a hack way of finding the minimum constant monthly min_payment 
    that will pay off debt in 1 year
    '''
    while fixed_payment_calc(balance, annualInterestRate, min_payment, month) > 0:
        min_payment = min_payment + 10
    
    return min_payment

print(min_payment_calculator(5000, 0.18, 100, 12))

def min_payment_calc_bisection(balance, annualInterestRate):
    '''
    uses bisection search to find the minimum constant monthly min_payment
    that will pay off debt it 1 year. 
    '''
    lower_bound = balance/12.0
    upper_bound = fixed_payment_calc(balance, annualInterestRate, 0, 12)/12.0
    guess = (upper_bound + lower_bound)/2.0

    while abs( fixed_payment_calc(balance, annualInterestRate, guess, 12)) > 0.01:
        if fixed_payment_calc(balance, annualInterestRate, guess, 12) > 0:
            #if our guess is too low, and we didnt' pay it all, then throw out 
            #anything below guess.. so our new lower bound is guess, and our
            #upper_bound is going to be what it was before
            lower_bound = guess
            guess = (upper_bound + lower_bound)/2.0
        else:
            upper_bound = guess
            guess = (upper_bound + lower_bound)/2.0


    return guess

print(min_payment_calc_bisection(5000, 0.18))




