#PROGRAM TO FIND  ROOTS OF QUADRATIC EQUATION
#Pushp Bhardwaj
import math
print("Enter the value of a,b,c in equation ax2 + bx + c")
a,b,c = [ int(x) for x in input().split() ]

D = b**2 - 4*a*c

if D >= 0:
    x = (-b + math.sqrt(D)) / 2*a
    y = (-b - math.sqrt(D)) / 2*a
else:
    x = complex( (-b/(2*a)), math.sqrt(-D)/(2*a))
    y = complex( (-b/(2*a)), -math.sqrt(-D)/(2*a))

if D > 0:
    print("This equation has two real roots: {} and {}".format(x,y))
elif D == 0:
    print("This equation has two equal roots: ", x)
else:
    print("This equation has two complex roots: {}  and {}".format(x,y))
