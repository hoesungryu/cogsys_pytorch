# lec_02 answer
# Q1. 
x[2]

# Q2. 
x[::-1]


# Q3. 
list_ = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for item in list_:
    if(item % 5 == 0):
        print(item)
        
# Q4.
lastNumber = 6
for row in range(1, lastNumber):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")
        
# Q5.   
n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()
    
# Q6 
F = [0, 1, 1]
for n in range(3, 23):
    f_n = F[n - 1] + F[n - 2]
    F.append(f_n)
print(F)

# Q7
x = [2.0, 3.0, 5.0, 7.0, 9.0]
Y = []
for v in x:
    new_val = (3.0 * v) ** 2 / (99 * v - v ** 3) - 1 / v
    Y.append(new_val)    

# one-liner with list-comprehension:
Y = [(3.0 * v) ** 2 / (99 * v - v ** 3) - 1 / v
     for v in x]

print(Y)
