# Default Value
base_price = 500000

rooms = int(input('Enter Apartment Number Of Rooms: '))
price_per_rooms = int(input('Enter Each Room Price: '))

print(f'The Apartment Money Amount is: {price_per_rooms * rooms + base_price}')
