# sum = 0
# for num in range(0, 101):
#     sum += num
# print(sum)
# 
# 
# 


# q = [[3, 4], [1, 2], [5, 6], [8, 7], [10, 9]]
# q = sorted(q)
# r = []
# e = []
# for interval in q:
#     a, b = interval
#     if not e:
#         e = [a, b]
#     else:
#         if a <= e[1]:
#             e[1] = max(e[1], b)
#         else:
#             r.append(e)
#             e = [a, b]
# r.append(e)
# print(r)
# 
# 

q = [[1, 4], [3, 6], [10, 9]]
q = [[min(a, b), max(a, b)] for a, b in q]
q = sorted(q)
r = []
e = []
for a, b in q:
    if not e:
        e = [a, b]
    else:
        if a <= e[1]:
            e[1] = max(e[1], b)
        else:
            r.append(e)
            e = [a, b]
r.append(e)
print(r)