def min_payment_calc(balance, annualInterestRate, monthlyPaymentRate):
    """this function returns the balance after you have payed the minimum monthly payment for 12 months"""

    for month in range(1, 13):

        min_payment = balance * 0.02
        # print("min payment = " + str(min_payment))

        unpaid_balance = balance - min_payment
        # print("unpaid balance = " + str(unpaid_balance))

        interest = (annualInterestRate / 12.0) * (unpaid_balance)
        # print("acrued insterest = " + str(interest))

        balance = unpaid_balance + interest
        # print("at month " + str(month) + " the balance is " + str(balance) + "\n")

    return balance


#print(min_payment_calc(5000, 1.0, 0.00001))


def payment_calc(balance, annualInterestRate, payment):
    """this function will return the balance after making 12 months of payments at a fixed rate"""

    for month in range(1, 13):

        unpaid_balance = balance - payment
        # print("unpaid balance = " + str(unpaid_balance))

        interest = (annualInterestRate / 12.0) * (unpaid_balance)
        # print("acrued insterest = " + str(interest))

        balance = unpaid_balance + interest
        # print("at month " + str(month) + " the balance is " + str(balance) + "\n")

    return balance


print(payment_calc(5000, 0.18, 625))


def min_payment_calc(balance, annualInterestRate):
    """this function will return the minimum fixed payment you will have to make per month in order to pay off the entire balance in 12 months"""

    payment = balance / 12.0

    while payment_calc(balance, annualInterestRate, payment) > 0:
        payment = payment + 5

    return payment


#print(min_payment_calc(5000, 0.18))


def bisection_min_payment_calc(balance, annualInterestRate):
    """this function will return the minimum fixed payment you will have to make per month in order to pay off the entire balance within 12 months... the catch is, it does it using BI-SECTION SEARCHHH!!"""

    lower_bound = balance / 12.0
    upper_bound = balance / 6.0
    payment = (upper_bound + lower_bound) / 2.0

    while abs(payment_calc(balance, annualInterestRate, payment)) >= 50:

        if payment_calc(balance, annualInterestRate, payment) > 0:
            payment = (payment + upper_bound) / 2.0
        elif payment_calc(balance, annualInterestRate, payment) < 0:
            payment = (payment + lower_bound) / 2.0
    return payment


#print(bisection_min_payment_calc(5000, 0.18))
