#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 10:55:33 2017

@author: metalinux
"""

# Fixed variables
portion_down_payment = 0.25
current_savings = 0
r = 0.04
number_of_months = 0

# User input variables
annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

# Computed variables
monthly_salary = annual_salary / 12
down_payment = total_cost * portion_down_payment

while current_savings < down_payment:
    if (number_of_months % 6) == 0 and number_of_months != 0:
        monthly_salary += monthly_salary * semi_annual_raise
    current_savings += current_savings * r / 12
    current_savings += monthly_salary * portion_saved
    number_of_months += 1

print("Number of months:", number_of_months)