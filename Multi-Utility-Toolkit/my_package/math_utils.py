"""Reusable math calculations."""
import math

def compound_amount(principal, rate, years):
    return principal * (1 + rate / 100) ** years

def circle_area(radius):
    return math.pi * radius ** 2

def rectangle_area(length, width):
    return length * width

def square_area(side):
    return side ** 2
