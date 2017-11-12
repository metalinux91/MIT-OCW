#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 11:09:55 2017

@author: metalinux
"""

# Fixed variables
portion_down_payment = 0.25
r = 0.04
number_of_months = 0
semi_annual_raise = 0.07
total_cost = 1000000
epsilon = 100
number_of_months = 36

# Ask the use for annual salary
annual_salary = int(input("Enter the starting salary: "))

# Calculate down payment based on total cost and down payment portion
down_payment = total_cost * portion_down_payment

# First, check if it is possible to make the down payment within 3 years
# If so, try to find the saving rate, otherwise iform that it is impossible
current_savings = 0
monthly_salary = annual_salary / 12
for i in range(number_of_months):
    if current_savings < down_payment:
        if (i % 6) == 0 and i != 0:
            monthly_salary += monthly_salary * semi_annual_raise
        current_savings += current_savings * r / 12
        current_savings += monthly_salary
    else:
        break

if current_savings < down_payment:
    print("It is not possible to pay the down payment in three years.")
else: 
    # Bisection search variables
    num_guesses = 0
    low = 0
    high = 10000
    portion_saved = (high + low) / 2.0
    found = False
    while not found:
        monthly_salary = annual_salary / 12
        current_savings = 0
        for i in range(number_of_months):
            if abs(current_savings - down_payment) >= epsilon:
                if (i % 6) == 0 and i != 0:
                    monthly_salary += monthly_salary * semi_annual_raise
                current_savings += current_savings * r / 12
                current_savings += monthly_salary * float(portion_saved / 10000)
            else:
                break
            
        if abs(current_savings - down_payment) >= epsilon:
            if current_savings < down_payment:
                low = portion_saved
            else:
                high = portion_saved
            portion_saved = (high + low) / 2.0
            num_guesses += 1
        else:
            found = True
    
    print("Best savings rate:", round(portion_saved / 10000, 4))
    print("Steps in bisection search:", num_guesses)
    