# cook your dish here
t=int(input())
while(t):
    x,y,z=map(int,input().split())
    print("yes" if (y+z*2)<=x else "no")
    t=t-1