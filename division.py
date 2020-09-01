import numpy as np
for num in np.arange(1,31):
	for deck in np.arange(1,6,.5):
		print('{}: {} '.format(num, deck) + str(num//deck))
		print('\n')


