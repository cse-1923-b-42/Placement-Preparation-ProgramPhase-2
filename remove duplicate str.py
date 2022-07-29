#to remove duplicates string

def check(x,k):
    for j in range(k,n):
        if x==name[j]:
            break
    return True

n = int(input("How many strings your want to enter"))
name = []
for i in range(n):
    name.append(input())

print(name)

i = 0
for i in range(n):
    if check(name[i],++i):
        del name[i]

print(name)
    
    
    
