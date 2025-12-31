n=int(input())
sum=0
# for i in range(1,n+1):
#     if i%2!=0:
#         sum+=i
i=0
while i<=n:
    if i%2!=0:
        sum+=i
    i+=1
print(sum)