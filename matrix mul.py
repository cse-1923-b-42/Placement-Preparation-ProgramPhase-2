a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

b = [[3,2,1],
     [6,5,4],
     [9,8,7]]

r = [[0,0,0],
     [0,0,0],
     [0,0,0]]

for x in range(len(a)):
    for y in range(len(b[0])):
        for z in range(len(b)):
            r[x][y] += a[x][z] * b[z][y]

for i in r:
    print(i)
            
