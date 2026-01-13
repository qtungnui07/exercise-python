s=input()
print(s.lower())
print(s.upper())
sum=0
chars=0
suma=0
sumt=0
for char in s:
    if s.isdigit():
        sum+=1
    if s.isalpha():
        chars+=1
    if char == "a":
        suma+=1
    if char == "t":
        sumt+=1
print(sum)
print(chars)
print(suma)
print(sumt)
words=s.split()
print(len(words))

        