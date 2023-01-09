ride_number_text= input('please enter the ride number you want: ')
ride_number = int(ride_number_text)
age=input('Please enter your age: ')
age= int(age)
if age < 1 or age > 95:
    print('You can not enter ride')
while ride_number < 1 or ride_number > 5:
    print('There is no ride with that number')
    ride_number_text = input('Please enter the ride number you want: ')
    ride_number = int(ride_number_text)
print('You have selected ride number:',ride_number)


