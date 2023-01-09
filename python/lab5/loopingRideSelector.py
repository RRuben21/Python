
import snaps

snaps.display_image('themepark.png')

prompt='''These are the available rides

1: Scenic River Cruise
2: Carnival Carousel
3: Jungle Adventure Water Splash
4: Downhill Mountain Run
5: The Regurgitator

Select your ride:'''



ride_number_text = snaps.get_string(prompt,vert='bottom',
                                    max_line_length=3)


while ride_number < 1 or ride_number > 5:
    print('There is no ride with that number')
    ride_number_text = input('Please enter the ride number you want: ')
    ride_number = int(ride_number_text)

print('You have selected ride number:',ride_number)
  
age=input('Please enter your age: ')
age= int(age)
if age < 1 or age > 95:
    print('You can not enter ride')
confirm='Ride ' + ride_number_text
snaps.display_message(confirm)
