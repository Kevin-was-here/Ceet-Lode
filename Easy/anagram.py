s = "anagram"
t = "nagaram"

if len(s) != len(t): print( False)

a = {}
b = {}

for i in range(len(s)):
    if s[i] in a.keys():
        a[s[i]] += 1
    else:
        a[s[i]] = 1

    if t[i] in b.keys():
        b[t[i]] += 1
    else:
        b[t[i]] = 1

if a == b:
    print( True)
else: print(False)