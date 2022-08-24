"""
Write a python script to check whether a given quadratic equation has two real &
distinct roots, real & equal roots or imaginary roots
"""

val_b,val_a,val_c=int(input('Enter Value of b : ')),int(input('Enter Value of a : ')),int(input('Enter Value of c : '))
equation_val=val_b**2-(4*val_a*val_c)

if equation_val>0:
    print('Roots are Real & Distinct')
elif equation_val<0:
    print('Roots are Imaginary')
else:
    print('Roots are Real & Equal')
