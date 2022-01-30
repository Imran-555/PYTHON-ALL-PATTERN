#SQUARE
print()
print("<----SQUARE---->")
for i in range(5):
    print("************")


#TRANGLE
print()
print("<----TRANGLE---->")
for i in range(0,6):
    for j in range(i):
        print("*",end="")
    print()


#TRANGLE
print()
print("<----TRANGLE---->")
for i in range(1,5):
    for j in range(2*i-1):
        print("*",end="")
    print()



#PYRAMID
print()
print("<----PYRAMID---->")
for i in range(1,5):
    for j in range(4-i):
        print(" ",end="")
    for k in range(0,(2*i)-1):
        print("*",end="")
    print()

#OPPOSITE PYRAMID
print()
print("<----OPPOSITE PYRAMID---->")
for i in range(-4,1):
    for j in range(4+i):
        print(" ",end="")
    for k in range(2*i+1,0):
        print("*",end="")
    print()

#UNIQUE PQTTERN
print()
print("<----UNIQUE PATTERN---->")
for i in range(1,5):
    for j in range(4-i):
        print(" ",end="")
    for k in range(0,(2*i)-1):
        print("*",end="")
    print()
for i in range(-4,1):
    for j in range(4+i):
        print(" ",end="")
    for k in range(2*i+1,0):
        print("*",end="")
    print()














