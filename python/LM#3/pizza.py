import math

students_text= input('How many students:')

students_int= int(students_text)

pizza_count= students_int/1.5

pizza_count= math.ceil(pizza_count)

print('You will need',pizza_count, 'pizzas')
