class car:
    def __init__(brand,manufacture,type, color):
        brand.manufacture=manufacture
        brand.type=type
        brand.color=color
        
        

    def vehicle(brand):
        return '{} {} {}'.format(brand.manufacture, brand.type, brand.color,)

car_1= car('Ford', 'Suv', 'Black')
car_2= car('Chevy', 'Truck', 'Green')
car_3= car('Dodge', 'Car', 'White')

car_1.vehicle()
car_2.vehicle()
car_3.vehicle()

print(car.vehicle(car_1))
print(car.vehicle(car_2))
print(car.vehicle(car_3))
