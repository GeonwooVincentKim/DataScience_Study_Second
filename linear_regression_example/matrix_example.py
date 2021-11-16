from typing import List


Matrix = List[List[float]]
print(Matrix)

A = [[1, 2, 3],
     [4, 5, 6]]

B = [[1, 2],
     [3, 4],
     [5, 6]]

for i in A:
    print("{0}".format(i))
    
    for j in i:
        print("{0}".format(j))    
    print("")

print("==================================")

for i in B:
    print("{0}".format(i))
    
    for j in i:
        print("{0}".format(j))
    print("")
