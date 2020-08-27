import numpy as np

def SomeExperiment(val1):
	print('Результаты измерений')
	def func():
		result = val1 + np.random.uniform(low=-1, high=1)
		return np.round(result, 2)
	text = ''
	for i in range(10):
		print('Результат ' + str(i) + ' измерения: ' + str(func()))
	return 


def AnotherExperiment():
	print('Следующий эксперимент')