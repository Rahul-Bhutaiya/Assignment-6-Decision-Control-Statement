#Write a python script to check whether a given year is a leap year or not.

year=int(input('Enter any Year : '))
print('It\'s Leap Year...' if year%400==0 else 'It\'s Not a Leap Year...' if year%100==0 else 'It\'s Leap Year...' if year%4==0 else 'It\'s Not a Leap Year...')