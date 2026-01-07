s = input().split()
u = []
for i in range(len(s)-1, -1, -1):
    u.append(s[i])

print(' '.join(u))


s = input().split()
u = ' '.join(s[::-1])
print(u)
