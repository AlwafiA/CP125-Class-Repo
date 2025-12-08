# Lab 02 Exercise 4: Dynamic Parking Rate
# Write your code below:

def get_hourly_rate(vehicle_type, hour_24):
    if vehicle_type =="Electric":
        rate = float(hour_24 * 2.00)
    

# Test your code here
print("Testing Dynamic Parking Rate...")




'''
Situation:

A parking system determines hourly rates dynamically:

Electric vehicles pay RM2.00/hour at all times.
Hybrid vehicles pay RM2.00/hour ONLY between 10pm (22) and 6am (6). Otherwise, they pay RM5.00/hour.
All Other vehicles pay RM5.00/hour at all times.
Task: Write a program that calculates and returns the correct hourly rate (float) based on vehicle type and hour.'''