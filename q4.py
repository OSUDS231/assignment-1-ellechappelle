# Author: Elle Chappelle
# GitHub Username: ellechappelle
# Date: 04/15/2026
# Description: This program takes a word from the user and prints the word after being manipulated in multiple ways

# Part one: store user input as a variable called "word"
word = input("Please enter a word: ")

# Part two: produce and print hints about the word
print(f"First character: {word[0]}")
print(f"Last character: {word[-1]}")
print(f"First four characters: {word[0:4:]}")
print(f"Every other character: {word[::2]}")
print(f"Backward: {word[::-1]}")