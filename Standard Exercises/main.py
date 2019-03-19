import sys
import datetime as dt
import math

#1: Write a Python program to print the following string in a specific format (see the output).
print('Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are')

#2: Write a Python program to get the Python version you are using.
print(sys.version_info[0])

#3: Write a Python program to display the current date and time.
print(dt.datetime.now())

#4: Write a Python program which accepts the radius of a circle from the user and compute the area.
def circle_area ():
    radius = input("Enter the radius of the circle: ")
    area = (float(radius) ** 2) * math.pi
    print(area)

#commenting out so it doesn't prompt every time
#circle_area()

#5: Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
def name_reverse ():
    first_name = input("Please input your first name: ")
    last_name = input("Please input your last name: ")
    reverse = str(last_name) + " " + str(first_name)
    print(reverse)

#commenting out so it doesn't prompt every time
#name_reverse()

#6: Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
