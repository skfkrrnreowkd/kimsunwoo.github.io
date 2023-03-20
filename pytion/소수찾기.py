n = int(input(''))
count = 0
num = []*n

num = (list(map(int,input('').split())))

#소수찾기
for i in num:
    if i == 1:
        continue

    button = 0

    for k in range(2,i):
        if i % k == 0:
            button = 1
            break

    if button == 0:
        count += 1
    
print(count)

