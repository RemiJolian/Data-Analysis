#Import lib
import numpy as np

#Create function
def calculate(my_lst:list) -> dict:
    numpy_lst = np.array(my_lst).reshape(3,3)
    d = dict()

    d['mean'] = numpy_lst.mean()
    d['variance'] = numpy_lst.var()
    d['standard deviation'] = numpy_lst.std()
    d['max'] = numpy_lst.max()
    d['min'] = numpy_lst.min()
    d['sum'] = numpy_lst.sum()
    return numpy_lst, d

my_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]
result = calculate(my_lst)
print(result)

