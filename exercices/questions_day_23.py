# You are given a string S and width W. Your task is to wrap the string into a paragraph of width.
import textwrap

string = str(input("Enter a string: "))
width_text = int(input("Enter a number of width: "))

text = textwrap.fill(string,width=width_text)
print(text)

# You are given a date. Your task is to find what the day is on that date.

import calendar

month, day, year = map(int, input("Enter date: ").split())
day_id = calendar.weekday(year, month, day)
print(calendar.day_name[day_id].upper())

