# Author: Elle Chappelle
# GitHub Username: ellechappelle
# Date: 04/15/2026
# Description: This program takes input in the form of seconds and outputs hours, minutes, and seconds

# Part one: store user input as variable named "total_seconds"
total_seconds = int(input("Please enter a number of seconds to convert into hours, minutes, seconds: "))

# Part two: convert user input to hours, minutes, and seconds
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds - (hours * 3600 + minutes * 60)

# Part three: print hours, minutes, and seconds
print(f"{total_seconds} seconds = {hours} hours, {minutes} minutes, {seconds} seconds")