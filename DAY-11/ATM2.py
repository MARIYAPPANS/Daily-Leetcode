# cook your dish here
t=int(input())
while(t):
    n,k=map(int,input().split())
    a=map(int,input().split())
    res=""
    for i in a:
        if k>=i:
            k=k-i
            res+="1"
        else:
            res+="0"
    print(res)
        
    t=t-1