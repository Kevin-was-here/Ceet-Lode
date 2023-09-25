numRows = 4
s = "PAYPALISHIRING"
numMidRows = numRows - 2
midRowIndexes = []

for i in range(numMidRows):
    midRowIndexes.append(numRows-2-i)


x = []
for i in range(numRows):
    x.append([''])

col = 0
while s != "":
    try:
        for i in range(numRows):
            x[i][col]= s[0]
            s = s[1:]

        for i in range(numMidRows):
            col += 1
            for j in range(numRows):
                x[j].append('')
            x[midRowIndexes[i]][col]=s[0]
            s = s[1:] 
            
        
        col += 1
        for i in range(numRows):
            x[i].append('')
    except:
        break

out = ''
for i in x:
    for j in i:
        if j != '':
            out += j

print(out)