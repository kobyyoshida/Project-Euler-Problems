def sum_of_squares(num):
    result = 0
    for i in range(num+1):
        result = result + i**2
    return result

def square_of_sums(num):
    result = 0
    for i in range(num+1):
        result = result + i
    return result**2

def difference(sum_osq,sq_os):
    return square_of_sums(sq_os) - sum_of_squares(sum_osq)

print("Difference = ",difference(100,100))