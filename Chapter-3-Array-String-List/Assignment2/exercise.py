#1
while True:
    s = input()
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not palindrome")
    c = input().lower()
    if c != "y":
        print("Thank you!")
        break
#2
s = input()
print(" ".join(s.split()))
#3
s = input()
nums = list(map(int, s.split(";")))
for x in nums:
    print(x)
even = 0
negative = 0
prime = 0

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for x in nums:
    if x % 2 == 0:
        even += 1
    if x < 0:
        negative += 1
    if is_prime(x):
        prime += 1

print(even)
print(negative)
print(prime)
print(sum(nums) / len(nums))
#4
s = input()
upper = lower = digit = special = space = vowel = consonant = 0
vowels = "aeiouAEIOU"

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
        if ch in vowels:
            vowel += 1
        else:
            consonant += 1
    elif ch.isdigit():
        digit += 1
    elif ch.isspace():
        space += 1
    else:
        special += 1

print(upper)
print(lower)
print(digit)
print(special)
print(space)
print(vowel)
print(consonant)
#5
def NegativeNumberInStrings(s):
    i = 0
    while i < len(s):
        if s[i] == "-" and i + 1 < len(s) and s[i + 1].isdigit():
            j = i + 1
            num = "-"
            while j < len(s) and s[j].isdigit():
                num += s[j]
                j += 1
            print(num)
            i = j
        else:
            i += 1

s = input()
NegativeNumberInStrings(s)
#6
s = input()
words = s.strip().lower().split()
res = []
for w in words:
    res.append(w.capitalize())
print(" ".join(res))
#7
def get_file_name(path):
    return path.split("\\")[-1]
def get_song_name(path):
    file = get_file_name(path)
    return file[:file.rfind(".")]
path = input()
print(get_file_name(path))
print(get_song_name(path))
