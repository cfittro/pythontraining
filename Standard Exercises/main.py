import sys
import datetime as dt
import math
import os

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
def comma_separated ():
    data = input("Please enter any number of comma separated values: ")
    list1 = data.split(",")
    tuple1 = tuple(list1)
    print("List version: ",list1)
    print("Tuple version: ",tuple1)

#commenting out so it doesn't prompt every time
#comma_separated()

#7: Write a Python program to accept a filename from the user and print the extension of that.
def file_extension ():
    filename = input("Please enter the full filename: ")
    etc, extension = os.path.splitext (filename)
    print(extension)

#commenting out so it doesn't prompt every time
#file_extension()

#8: Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]

print(color_list[0],color_list[-1])

#9: Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)

print("The examination will start from: %i/%i/%i"%exam_st_date)

#10: Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
def raised_twice ():
    value = input("Please input an integer: ")
    calculation = int(value) + int(value*2) + int(value*3)
    print(calculation)

#commenting out so it doesn't prompt every time
#raised_twice()
