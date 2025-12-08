# Lab 02 Exercise 2: Camping Logistics
# Write your code below:

import math

def calculate_event_cost(participants, tent_capacity, tent_price, meal_price):
    tents_needed = math.ceil(participants / tent_capacity)
    total_price = tents_needed * tent_price
    total_cost = participants * meal_price
    final_total = total_cost + total_price

    return final_total

