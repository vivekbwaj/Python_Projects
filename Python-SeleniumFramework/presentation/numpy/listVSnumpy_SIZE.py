import numpy as np
import sys

my_list=range(1000)
print(sys.getsizeof(5)*len(my_list))

var_numpy=np.arange(1000)
print(var_numpy.size*var_numpy.itemsize)