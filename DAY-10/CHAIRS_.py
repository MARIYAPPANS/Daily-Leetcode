# cook your dish here
t=int(input())
while(t):
    x,y=map(int,input().split())
    if y<x:
        print(x-y)
    else:
        print(0)
    t=t-1