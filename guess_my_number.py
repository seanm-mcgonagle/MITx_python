

print ("Please think of a number between 0 and 100!")

high = 100
low = 0
epsilon = 0.001
ans = (high + low) / 2.0

guess = 'whatevs'

while guess != 'c':

    ans = (high + low) / 2.0

    guess = input("Is your secret number %s? If it's too high, type 'h'. If it's too low, type 'l'. If my guess is correct, then type 'c'\n" % (ans))

    if guess == 'h':
        high = ans
    elif guess == 'l':
        low = ans
    elif guess == 'c':
        break

print ("Game over.Your secret number was: %s!" % (round(ans)))
