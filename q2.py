# Author: Elle Chappelle
# GitHub Username: ellechappelle
# Date: 04/15/2026
# Description: This program takes the dimensions of a rectangle from the user and outputs the area, perimeter, and diagonal length

# Part one: store user input of rectangles dimensions as variables "length" and "width"
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

# Part two: compute rectangle characteristics
area = length * width
perimeter = (length * 2) + (width * 2)
diagonal = (length**2 +width**2)**0.5

# Part two: produce summary of rectangle with rounded values
print("Rectangle summary: ")
print(f"Area: {round(area, 1)}")
print(f"Perimeter: {round(perimeter, 1)}")
print(f"Diagonal: {round(diagonal, 2)}")