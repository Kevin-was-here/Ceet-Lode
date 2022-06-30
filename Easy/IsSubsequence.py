s = "aaaaaa"
t = "bbaaaa"

# 44% solution 
s = list(s)
t = list(t)
out = True
slen = len(s)

for i in s:
    if i in t:
        index = t.index(i)
        t = t[index:]
        slen -= 1
        if len(t) < slen:
            out = False
            break
    else:
        out = False
        break
        
print(out)

