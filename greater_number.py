"""
Write a python script to print greater between two numbers. Print number only once
even if the numbers are the same.
"""

val_1=int(input('Enter First Number : '))
val_2=int(input('Enter Second Number : '))

print(val_1 if val_1>val_2 else val_2)