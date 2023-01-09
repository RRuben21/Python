age_text=input('what is your age?: ')
age= int(age_text)

active= True
while active:
    
    if age <= 3:
        print('The Movie ticket is free')
    if age > 3 and age<=12:
        print('The Movie ticket is 10$')
    if age > 12:
        print('The Movie ticket is 15$')
    break
