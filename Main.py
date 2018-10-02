value = int(input('Введите трехзначное число'))

if (value < 1000 and value >= 100):
	Num1 = value % 10
	Num2 = value % 100 .. 10
	Num3 = value // 100
	Sum = Num1 + Num2 + Num3
	print('Sum = ', Sum)
else:
	print('Число не является трехзначным')

if Sum % 2 == 0:
	print('True')
else:
	print('False')
