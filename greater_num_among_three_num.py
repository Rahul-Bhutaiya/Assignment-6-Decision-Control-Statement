"""
Write a python script to print greater among three numbers. Print number only once
even if the numbers are the same.
"""

number_1,number_2,number_3=int(input('Enter First Number : ')),int(input('Enter Second Number : ')),int(input('Enter Third Number : '))

#METHOD:1
"""
if number_1>number_2:
    if number_1>number_3:
        print(number_1)
    else:
        print(number_3)
else:
    if number_2>number_3:
        print(number_2)
    else:
        print(number_3)
"""

#METHOD:2
print((number_1 if number_1>number_3 else number_3) if number_1>number_2 else (number_2 if number_2>number_3 else number_3))
