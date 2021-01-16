#Slow run time

primes = [2,3,5,7]

def check_prime(num):
    for prime in primes:
        if num%prime == 0:
            break
        elif prime == primes[len(primes)-1]:
            primes.append(num)
            #print("PRIME ARRAY: ",primes)

def get_prime_sum():
    result = 0
    for i in primes:
        result = result + i
    return result

for num in range(7,2000000,2):
    check_prime(num)

s = get_prime_sum()

print("Sum = ",s)