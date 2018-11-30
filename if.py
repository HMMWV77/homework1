age = int(input('Возраст:'))
if age < 7:
	print('Детский сад')
elif 7 < age < 18:
	print('Школа')
elif 18 < age < 25:
	print('Университет')
elif age > 25:
	print('Работа')