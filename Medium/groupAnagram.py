strs = ["eat","tea","tan","ate","nat","bat"]
x = {}

for i in strs:
    sorti = ''.join(sorted(i))

    if sorti in x.keys():
        x[sorti].append(i)
    else:
        x[sorti] = [i]

out = []
for i in x.keys():
    out.append(x[i])

print(out)