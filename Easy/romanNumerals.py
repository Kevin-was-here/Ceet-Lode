#70% sol
s = "MCMXCIV"
out = 0
prev = ""
ref = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

for i in range(len(s)-1,-1,-1):
    out += ref[s[i]]
    if (s[i] == "I" and (prev == "V" or prev == "X")):
        out -=2
    elif(s[i] == "X" and (prev == "L" or prev == "C")):
        out -=20
    elif(s[i] == "C" and (prev == "D" or prev == "M")):
        out -=200
    prev = s[i]

print(out)