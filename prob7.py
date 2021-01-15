#Unfinished

primes = [2,3,5,7,11,13]
current_num=13


while len(primes) <= 10002:
    for prime in primes:
        if current_num%prime == 0:
            current_num+=1
        else:
            primes.append(current_num)
            current_num+=1
        

print(primes[10000])
