#Import lib
import numpy as np

#Create function
def calculate(my_lst:list) -> dict:
    if len(my_lst) != 9:
        raise ValueError ('List must contain nine numbers.')
    numpy_lst = np.array(my_lst).reshape(3,3)
    d = dict()

    d['mean'] = [numpy_lst.mean(axis=0).tolist(),numpy_lst.mean(axis=1).tolist(),numpy_lst.mean()]
    d['variance'] = [numpy_lst.var(axis=0).tolist(),numpy_lst.var(axis=1).tolist(),numpy_lst.var()]
    d['standard deviation'] = [numpy_lst.std(axis=0).tolist(),numpy_lst.std(axis=1).tolist(),numpy_lst.std()]
    d['max'] = [numpy_lst.max(axis=0).tolist(),numpy_lst.max(axis=1).tolist(),numpy_lst.max()]
    d['min'] = [numpy_lst.min(axis=0).tolist(),numpy_lst.min(axis=1).tolist(),numpy_lst.min()]
    d['sum'] = [numpy_lst.sum(axis=0).tolist(),numpy_lst.sum(axis=1).tolist(),numpy_lst.sum()]
    return d

my_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]
result = calculate(my_lst)
print(result)

# d ={
#   'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
#   'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
#   'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
#   'max': [[6, 7, 8], [2, 5, 8], 8],
#   'min': [[0, 1, 2], [0, 3, 6], 0],
#   'sum': [[9, 12, 15], [3, 12, 21], 36]
# }

