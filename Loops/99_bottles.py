"""20. 99 Bottles
# Squares
On May 6th, 1949, EDSAC, an early electronic stored-program computer, ran its first program at the University of Cambridge.

It calculated and printed out a list of squares:

0   0
1   1
2   4
3   9
4   16
5   25
6   36
7   49
8   64
9   81

On the left, you got all the single-digit numbers from 0 to 9. On the right are their squares. For example, in the last row, 9 × 9 = 81.

This can be done in Python using string concatenation:

# String concatenation

for i in range(5):
  print('The square of ' + str(i) + ' is ' + str(i*i))

The output would look like:

The square of 0 is 0
The square of 1 is 1
The square of 2 is 4
The square of 3 is 9
The square of 4 is 16

# String Interpolation
Let's learn a new tool that's very similar to string concatenation, before continuing on to the instructions.

String interpolation is a process of substituting values of variables into placeholders in a string.

For instance, if you have a template for saying hello to a person in an email like 'Hi {name}, nice to meet you!', you would like to replace the placeholder {name} with an actual name. This is string interpolation.

The above program can be recreated using string interpolation using the {} sign:

# String interpolation

for i in range(5):
  print(f'The square of {i} is {i*i}')

Notice the f prefix before the quotes.

Instructions
"99 Bottles of Beer" is an old song that annoying kids, oops I mean everyone, sang on road trips to pass the time.

Create a 99_bottles.py program and use a for loop and a range() function to print out all the verses of "99 Bottles of Beer."

99 bottles of beer on the wall

99 bottles of beer

Take one down, pass it around

98 bottles of beer on the wall

And don't forget to use string interpolation!"""



# Write code below 💖
for i in range(99,0,-1):
  print(f'{i} bottles of beer on the wall')
  print(f'{i} bottles of beer')
  print(f'Take one down, pass it around')
  i=i-1
  print(f'{i}  bottles of beer on the wall')