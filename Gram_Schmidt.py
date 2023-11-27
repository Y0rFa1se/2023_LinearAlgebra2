from itertools import *
from Matrix_Vector import *

n = int(input())
A = Matrix([]).random_square(n)
while not (A.is_invertible()):
    A = Matrix([]).random_square(n)

Q = Matrix([])

for a in A:
    for q in Q:
        a -= q * q.inner_product(a)
        
    Q = Q.append(a.normalization())
    
print("Q")
print(Q.transpose())
print()

print("|Q|")
for q in Q:
    print(q.absolute())
print()
    
print("orthogonal")
for a, b in combinations(Q, 2):
    print(a.inner_product(b))
print()