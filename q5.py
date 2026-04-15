# Author: Elle Chappelle
# GitHub Username: ellechappelle
# Date: 04/15/2026
# Description:

# PART (A): store user input about trip distance, average speed, fuel efficiency, and gas price and variables
trip_distance = float(input("Enter the trip distance (miles): "))
average_speed = float(input("Enter the average speed (mph): "))
fuel_efficiency = float(input("Enter the fuel efficiency (mpg): "))
gas_price = float(input("Enter the gas price per gallon: "))
# notes: float doesn't work, can't multiply by non-int type

# PART (B): compute total driving time, gas needed, and total fuel cost
driving_time = round(float(trip_distance / average_speed), 1)
gas_needed = round(float(trip_distance / fuel_efficiency), 1)
fuel_cost = round(float(gas_needed * gas_price), 1)

# PART (C): print trip summary
print()
print(f"For a trip of {round(trip_distance, 1)} miles at an average speed of {round(average_speed, 1)} mph, the driving time will be {driving_time} hours.")
print()
print(f"Your car will use {gas_needed} gallons of gas, and the total fuel cost will be ${fuel_cost}.")