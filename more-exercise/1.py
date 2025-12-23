n,x=map(int,input().split())
current=x
for i in range(0,n+1):
    row=[]
    for _ in range(i):
        row.append(current)
        current+=x
    print(*(row)) #* de bo cai dau ngoac vuong
        
        
        