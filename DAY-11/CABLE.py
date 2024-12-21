# cook your dish here
x,y,z,m=map(int,input().split())

if (x*y*z)>(m**3):
    print("cuboid")
elif (x*y*z)==(m**3):
    print("equal")
else:
    print("cube")