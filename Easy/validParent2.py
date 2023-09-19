s = "(){}[]"

x = {
    '}':'{',
    ']':'[',
    ')':'(',
}

a = []

for i in s:

    if i in ['(','{','[']:
        a.append(i)
    else:
        if a[-1] != x[i]:
            print(False)
        else: a.pop(-1)

if len(a) == 0:
    print(True)
else: print(False)
