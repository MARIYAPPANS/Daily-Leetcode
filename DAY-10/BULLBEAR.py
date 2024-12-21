# cook your dish here
t=int(input())
while(t):
    x,y=map(int,input().split())
    if x<y:
        print("profit")
    elif x==y:
        print("Neutral")
    else:
        print("loss")
    t=t-1