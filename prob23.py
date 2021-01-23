dictionary = {}

for i in range(1,28123):#Form dictionary with value of list(divisors)
    for j in range(1,round(i/2)):
        if i % j == 0:
            dictionary[i].append(j)
    
