import numpy as np
import time

SIZE=1000000

L1=range(SIZE)
L2=range(SIZE)

NP1=np.arange(SIZE)
NP2=np.arange(SIZE)

start=time.time()
list_result=[x + y for x, y in zip(L1, L2)]
print((time.time()-start)*1000)

start1=time.time()
n_result=NP1+NP2
print((time.time()-start1)*1000)