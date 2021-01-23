def factorial(n):
    product = 1
    for i in range(2,n+1):
        product *= i
    return product

def summ(n):
    num = 0
    for digit in n:
        num += int(digit)
    return num

print("Sum of digits in 100!: ",summ(str(factorial(100))))

