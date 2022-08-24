#Write a python script to check whether a given number is divisible by 5 or not

#METHOD:1
#print('Divisible' if int(input('Enter a Number : '))%5==0 else 'Not-Divisible')

#METHOD:2
number=input('Enter a Number : ')
print('Divisible' if number[len(number)-1]=='0' or number[len(number)-1]=='5' else 'Not-Divisible')