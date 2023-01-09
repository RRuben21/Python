my_str = input('Type a number:')

try:
    if my_str.isdigit():
        my_num = int(my_str)
        print('Number is an Integer')
    else:
        my_num = float(my_str)
        print('Number is a Float')
except ValueError:
    print('Please type a number...')

finally:
    print('Thank you!')


    

