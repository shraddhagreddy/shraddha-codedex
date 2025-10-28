"""
Instructions
The year is 2199... we have become an interplanetary species and can travel to other planets in the solar system! 🚀

Create a weight conversion program that:

Asks the user what their Earth weight is (as a float).
Asks the user for a planet number (as an int).
Then, use an if/elif/else statement to calculate the user's weight on the destination planet.

To calculate the user's weight:

destination weight=Earth weight × relative gravity
Number	Planet	Relative Gravity
1	Mercury	0.38
2	Venus	0.91
3	Mars	0.38
4	Jupiter	2.53
5	Saturn	1.07
6	Uranus	0.89
7	Neptune	1.14
If the user enters a planet number outside of 1 - 7, print a message that says 'Invalid planet number'.

"""

# Write code below 💖
earth_weight=float(input("enter ur weight on earth"))
planet=int(input("enter the planet number"))
if planet==1:
  rg=0.38
elif planet==2:
  rg=0.91
elif planet==3:
  rg=0.38
elif planet==4:
  rg=2.53
elif planet==5:
  rg=1.07
elif planet==6:
  rg=0.89
elif planet==7:
  rg=1.14
else:
  print("Invalid planet number.")

destination_weight=earth_weight*rg
print(destination_weight)