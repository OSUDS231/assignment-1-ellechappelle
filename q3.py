# Author: Elle Chappelle
# GitHub Username: ellechappelle
# Date: 04/15/2026
# Description:

# Get the input
total_seconds = int(input("Please enter a number of seconds to convert into hours, minutes, seconds: "))

# Hours = seconds / 3600
hours = total_seconds // 3600

# Minutes = remaining seconds / 60
minutes = (total_seconds % 3600) // 60

# Seconds = remaining seconds
seconds = total_seconds - (hours * 3600 + minutes * 60)

print(f"{total_seconds} seconds = {hours} hours, {minutes} minutes, {seconds} seconds")