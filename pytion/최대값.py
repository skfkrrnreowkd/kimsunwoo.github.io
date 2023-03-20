a=[]*9

for i in range (9):
    a.append(int(input("")))

max = 0

for j in range (9-max):
    if a[max] < a[j]:
        max = j
    
print(a[max])
print(max+1)