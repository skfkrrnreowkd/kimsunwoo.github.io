n , m = map(int,input("").split())

for i in range(n):
    for j in range(n):
        if i != j:
            print(i+1, j+1)
        
            