import sys
import datetime as dt
import math
import os
import calendar
from fractions import Fraction as fr

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

#11: Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s). 
print(abs.__doc__)

#12: Write a Python program to print the calendar of a given month and year. Note :Use 'calendar' module. 
def month ():
    y = int(input("Input the desired year: "))
    m = int(input("Input the desired month: "))
    calendar.prmonth(y,m)

#commenting out so it doesn't prompt every time
#month()

#13: Write a Python program to print the following here document.
print("""a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example""")

#14: Write a Python program to calculate number of days between two dates.
def datediff():
    start_string = input("Input the start date (YYYY-MM-DD): ")
    end_string = input("Input the end date (YYYY-MM-DD): ")
    start_year, start_month, start_day = map(int, start_string.split("-"))
    end_year, end_month, end_day = map(int, end_string.split("-"))
    start_date = dt.date(start_year,start_month,start_day)
    end_date = dt.date(end_year,end_month,end_day)
    delta = end_date - start_date
    print(delta.days)

#commenting out so it doesn't prompt every time
#datediff()

#15: Write a Python program to get the volume of a sphere with radius 6.
volume = math.pi * (6**3) * fr(4,3)
print(volume)
