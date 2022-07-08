str = ["ccc","acc","c"]

out = ""
i = 0
cur = (str[0])[i]

while True:
    if all(cur in string[:i+1] for string in str):
        out = cur
        i += 1
        cur += (str[0])[i]
    else: 
        print(out)
        break
