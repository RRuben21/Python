x=input('Type a number: ')
y=input('Type another number: ')
try:
    sum=float(x)+float(y)
    print('The sum is:',(sum))
except ValueError:
    print("Oops! That is not a number. Try again....")
        
finally:
    print('Thank you!')

