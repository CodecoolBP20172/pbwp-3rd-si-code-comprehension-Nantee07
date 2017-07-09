import random  # Importing the random module 

guessesTaken = 0  # Assign 0 to "guessesTaken" variable

print('Hello! What is your name?')  # Print the given string: 'Hello! What is your name?'
myName = input()  # Assign the user's input to the "myName" variable

number = random.randint(1, 20)  # Assign a randomly generated number from 1 to 20 to the "number" variable
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # Print the given string with the use of the user's answer 

while guessesTaken < 6:  # Loop until the value of the "guessesTaken" variable is less than 6
    print('Take a guess.')  # Print the given string: 'Take a guess.'
    guess = input()  # Assign the user's input to the "guess" variable
    guess = int(guess)  # Convert the value of the "guess" variable into an integer

    guessesTaken += 1  # Add +1 to the value of the "guessesTaken" variable

    if guess < number:  # If the given condition is True runs the following action
        print('Your guess is too low.')  # Print the given string: 'Your guess is too low.'

    if guess > number:  # If the given condition is True runs the following action
        print('Your guess is too high.')  # Print the given string: 'Your guess is too high.'

    if guess == number:  # If the values of "guess" and "number" variables are equal runs the following action
        break  # Break the loop

if guess == number:  # If the values of the "guess" and "number" variables are equal runs the following actions
    guessesTaken = str(guessesTaken)  # Convert the value of the "guessesTaken" variable into string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  # Print the given string with the use of the user's answer and the number of guesses the user made

if guess != number:  # If the value of "guess" and "number" variables are NOT equal runs the following actions
    number = str(number)  # Convert the value of the "number" variable into a string
    print('Nope. The number I was thinking of was ' + number)  # Print the given string with the use of the randomly generated number
