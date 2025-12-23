#hang so le di xuoi
#hang so chan di nguoc
n=int(input())
def zic_zac(x):
    val=1
    for i in range(x):
        row=[]
        for _ in range(x):
            row.append(val)
            val+=1
        if i%2!=0:
            row.reverse()
        print(*(row))
zic_zac(n)
