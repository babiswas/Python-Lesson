l=[[1,2,3],[4,5,6],[7,8,9]]
from functools import reduce
k=reduce(lambda l1,l2:l1+l2,l)
print(k)