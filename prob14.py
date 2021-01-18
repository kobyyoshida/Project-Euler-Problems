def even(num):
    return num/2

def odd(num):
    return (3*num)+1

def process_num(num,chain):
    print("CHAIN CHECK: ",chain)
    if num == 1:
        print("DONE")
        return chain
    elif num % 2 == 0:
        chain+=1
        num = process_num(even(num),chain)
    elif num % 2 != 0:
        chain+=1
        num = process_num(odd(num),chain)

for i in range(2,1000000):
    chain = 0
    chain = process_num(i,chain)
    print("NUMBER: ",i)
    print("CHAIN LENGTH: ",chain)