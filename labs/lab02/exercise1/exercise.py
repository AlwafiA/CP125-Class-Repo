# Lab 02 Exercise 1: Road Trip Budgeter
# Write your code below:

def is_budget_sufficient(length_km, km_per_liter, price_per_liter, budget): #receive and calculate input
    litres = (length_km*2 / km_per_liter)
    fuel_cost = price_per_liter * litres

    if fuel_cost > budget :
        return False
    else :
        return True

