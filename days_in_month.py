#Write a python script to take the month value in numeric format and display the number of days in it.

month_val=int(input('Enter Month : '))

if month_val==1 or month_val==3 or month_val==5 or month_val==7 or month_val==8 or month_val==10 or month_val==12:
    print('Days :',31)
elif month_val==4 or month_val==6 or month_val==9 or month_val==11:
    print('Days :',30)
elif month_val==2:
    print('Days :',28,'or',29)
else:
    print('Enter Valid Input')