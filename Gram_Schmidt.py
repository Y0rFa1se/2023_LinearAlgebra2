from itertools import *
from Matrix_Vector import *

m, n = map(int, input("m x n: ").split())
A = Matrix([])
for i in range(m):
    A = A.append(Vector(list(map(int, input(f"a_{i + 1}: ").split()))))
    
Q = Matrix([])

for a in A:
    for q in Q:
        a -= q * q.inner_product(a)
        
    Q = Q.append(a.normalization())
    
for a, b in combinations(Q, 2):
    print(a.inner_product(b))