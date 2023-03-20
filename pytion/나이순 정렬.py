n = int(input(''))
box = []*n

box.append(list(input('').split()))
    
for i in range(n):
    big = 0
    if box[big][0] < box[big][0]:
        box[big][0],box[big][0] = box[big][0],box[big][0]

print(box)
