# lec_05 answer

# Q1. 
{'env'+str(i[0]):list(i[1]) for i in enumerate(zip(loc,est),start=1)}

# Q2. 
print(set([i*j for i in range(1,10) for j in range(1,10)]),end=' ')

# Q3. 

["{0}*{1} = {2}".format(x,y,x*y)
 for x in range(1,10) for y in range(1,10) if x%2 == 0 and y%2 == 0]


# Q4. 
[[w.upper(),len(w)] for w in txt.split(" ")]


# Q5. 
{c+1:w for c,w in enumerate(txt.split(' '))}

