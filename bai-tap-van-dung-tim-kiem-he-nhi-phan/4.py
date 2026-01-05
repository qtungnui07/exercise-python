import sys

class Logger:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "a", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

log_file = __file__.replace(".py", ".txt")
sys.stdout = Logger(log_file)
sys.stderr = sys.stdout
n=int(input("n="))
a=list(map(int,input("nhap mang: ").split()))
for i in range(1,len(a)):
    key=a[i]
    j=i-1
    while j>=0 and key>a[j]:
        a[j+1]=a[j]
        j-=1
    a[j+1]=key
print(a)
x=int(input("x="))
print(bs_desc(a,x))