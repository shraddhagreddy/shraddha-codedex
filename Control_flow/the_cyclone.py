height = int(input("What is your height? "))
credits = int(input("How many credits do you have? "))

if height > 5 and credits > 10:
    print("Enjoy the ride!")
elif credits > 10 and height <= 5:
    print("You are not tall enough to ride.")
elif height > 5 and credits <= 10:
    print("You don't have enough credits.")
else:
    print("You did not meet either requirement.")
