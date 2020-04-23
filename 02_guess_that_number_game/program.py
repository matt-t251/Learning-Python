import random

print('-----------------------------')
print('   guess that number game')
print('-----------------------------')
print()

the_number = random.randint(0, 100)
guess = -1
while guess != the_number:

    guess_text = input('Guess a number between 0 and 100: ')

    guess = int(guess_text)

    if guess < the_number:
        print('your guess of {} too low'.format(guess))
    elif guess > the_number:
        print('your guess of {} too high'.format(guess))
    else:
        print('YOU WIN! {} is the right number.'.format(guess))
