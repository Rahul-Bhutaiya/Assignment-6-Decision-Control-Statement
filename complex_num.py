"""
Write a python script to accept one complex number from the user and display the
greater number between real part and imaginary part
"""

complex_num=complex(input('Enter a Complex Number : '))
print('Real_Part :',complex_num.real,'\nImaginary_Part :',complex_num.imag)
print('Greater Number :',complex_num.real if complex_num.real>complex_num.imag else complex_num.imag)