"""21. Fizz Buzz
# Congrats!
You've made it to the end of this chapter! Let's do a recap. 🥳

The while loop iterates over and over again while the condition is true:

while coffee < 1:
  print('Tired')

The for loop and the range() function to iterate for a certain number of times:

for i in range(10):
  print(i)

Now let's take your learnings to the test!

Instructions
Fizz Buzz is a children's word game that teaches division. It's also a classic technical interview question at countless companies. 🐝



Though this challenge may appear simple to experienced coders, it is designed to weed out 90% of job candidates who cannot apply their coding knowledge to a new problem creatively. Want to give it a try?

Create a fizz_buzz.py program that outputs numbers from 1 to 100.

Here's the catch:

For multiples of 3, print "Fizz" instead of the number.
For multiples of 5, print "Buzz" instead of the number.
Here's the tricky part: For multiples of 3 and 5, print "FizzBuzz".
The output should look like:

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
...

Btw, it's totally okay if you can't get this one... it's a tough problem! Take a look at the hint and the solution before moving forward to the Checkpoint Project! ⛳️


"""


# Write code below 💖
for i in range (1,100,1):
  if(i%3==0 and i%5==0):
    print("FizzBuzz")
  elif(i%5==0):
    print("Buzz")
  elif(i%3==0):
    print("Fizz")
  else:
    print(i)