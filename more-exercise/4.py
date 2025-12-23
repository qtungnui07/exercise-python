def ma_tran_doi_xung(row, height):
    space="  "*(height-row)
    left=list(range(row,1,-1))
    right=list(range(2,row+1))
    full=left + [1] + right
    print(space+" ".join(map(str, full)))
n=int(input())
for i in range(n,0,-1):
    ma_tran_doi_xung(i,n)

