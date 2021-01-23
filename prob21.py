am_sums = {}
amicables = []
def sum_divisors(num):
    divs = []
    for i in range(1,num):
        if num % i == 0:
            divs.append(i)
    summ = sum(divs)
    return summ

for i in range(1,10001):
    am_sums[i] = sum_divisors(i)

for num1,sum1 in am_sums.items():
    for num2, sum2 in am_sums.items():
        if sum1 == num2 and sum2==num1 and num1 != num2: 
            amicables.append(num1)
            amicables.append(num2)

print("TOTAL SUM: ",int(sum(amicables)/2))
