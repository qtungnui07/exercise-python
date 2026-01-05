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

arrin=list(map(int,input().split()))
def tgt(arr):
    if not arr:
        return
    if len(arr)>1:
        newarr=[arr[i]+arr[i+1] for i in range(len(arr)-1)]
        tgt(newarr)
    print(arr)
        
tgt(arrin)
log 