i = []
with open("file.txt", 'r') as fname:
    for lineas in fname:
        i.append(lineas.split())
b = len(i)

j = 0
while j < b:
    k = j +1
    while k < b:
        aux = set((i[j][2]).split(','))
        aux2 = set((i[k][2]).split(','))
        if (aux) & (aux2):
            print((i[j][0]),"-",(i[k][0]),":", len((aux) & (aux2)))
        k += 1
    j += 1
