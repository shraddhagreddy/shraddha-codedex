# Write code below 💖
"""# While Loop
Now that we got a sneak peek of a while loop, let's see what it does! 🔄

A while loop looks very similar to an if statement. Just like an if statement, it executes the code if the condition is True.

However, the difference is that the while loop will continue to execute the code inside of it, over and over again, as long as the condition is True.

while condition:
  # code inside

In other words, instead of executing once if a condition is true, it executes again and again while that condition is true.

Here, we have a while loop that asks the user to guess a number:

guess = 0

while guess != 6:
  guess = int(input('Guess the number: '))

This will run over and over again until the user guesses the number 6:

Guess the number: 5
Guess the number: 3
Guess the number: 6

The variable guess starts at 0 on the first line and then the program enters the while loop:

It checks the condition: is it true that 0 doesn't equal 6? Yep. Okay, run the code inside.
It checks the condition again: is it true that 5 doesn't equal 6? Yep. Okay, run the code inside.
It checks the condition again: is it true that 3 doesn't equal 6? Yep. Okay, run the code inside.
It checks the condition again: is it true that 6 doesn't equal 6? Nope! So it exits the while loop and skips the code inside.
To reiterate (no pun intended), at the beginning of each "loop", the condition is checked. The moment the condition becomes false, the program exits the while loop and continues on from the line after it.

Note: If the condition is False from the get-go, then the code block wouldn't run at all and will be skipped.

Instructions
Let's continue on from the code above.

Create a guess.py program and type in the following:

guess = 0

while guess != 6:
  guess = int(input("Guess the number:  "))

print("You got it!")

Run the code a few times so that you understand what it does.

Let's make it so that it's the same guessing game, but there is a new limit to the number of tries (it was infinite before).

First, introduce a variable called tries at the top and give it a value of 0.

Then, add a second condition with the tries variable to the while loop using a relational operator."""

guess=0
tries=0

while guess!=6:
  guess=int(input("guess the number:"))
  tries=tries+1
  while tries==4:
    print("exceeded number of tries")
    quit()
print("you got it!!")