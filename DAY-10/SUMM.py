# cook your dish here
t=int(input())
while(t):
    x,y,z=map(int,input().split())
    print("yes" if x+y==z else "no")
    t=t-1