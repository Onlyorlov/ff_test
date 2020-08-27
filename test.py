def SomeExperiment(val1):
	print('Результаты измерений')
	def func():
		return val1
	text = ''
	for i in range(10):
		print('Результат ' + str(i) + ' измерения: ' + str(func()))
	return 


def AnotherExperiment():
	print('Хуйня какая-то')
