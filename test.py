import numpy as np

def SomeExperiment(val1):
	print('Результаты измерений')
	def func(val):
		result = val + np.random.uniform(low=-1, high=1)
		return np.round(result, 2)
	text = ''
	for i in range(10):
		print('Результат ' + str(i) + ' измерения: ' + str(func(val1)))
	return 


def AnotherExperiment():
	print('Следующий эксперимент')