def min_payment_calc(balance, annualInterestRate, monthlyPaymentRate):

    for month in range(1, 13):

        min_payment = balance * 0.02
        print("min payment = " + str(min_payment))

        unpaid_balance = balance - min_payment
        print("unpaid balance = " + str(unpaid_balance))

        interest = (annualInterestRate / 12.0) * (unpaid_balance)
        print("acrued insterest = " + str(interest))

        balance = unpaid_balance + interest
        print("at month " + str(month) + " the balance is " + str(balance) + "\n")

    return balance


print(min_payment_calc(5000, 0.18, 0.02))


def fixed_payment(balance, annualInterestRate):
    guess_monthy_payment = balance / 12.0
    epsilon = 5

    while abs(balance - guess_balance) >= epsilon

        for month in range(1, 13):
            unpaid_balance = balance - guess_monthy_payment
            interest = (annualInterestRate / 12.0) * (unpaid_balance)
            balance =

        guess_balance = guess_balance + 1
