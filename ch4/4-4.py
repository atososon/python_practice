x = []
for i in list(range(0,10,2)):
    x.append(i)    
print(x)
y = [i for i in range(10) if i%2 == 0]
print(y)