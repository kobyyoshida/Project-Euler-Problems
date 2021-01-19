import operator

highest = 0
memory = {}

def even(num):
    return num/2

def odd(num):
    return (3*num)+1

def process_num(num,chain):
    #print("CHAIN CHECK: ",chain)
    if num == 1:
        #print("DONE")
        return int(chain)
    elif num % 2 == 0:
        if num in memory:
            return chain+memory[num]
        else:
            chain+=1
            return process_num(even(num),chain)
    elif num % 2 != 0:
        if num in memory:
            return chain+memory[num]
        else:
            chain+=1
            return process_num(odd(num),chain)

for i in range(2,1000001):
    chain = 0
    chain = process_num(i,chain)
    memory[i] = chain
    #if chain > highest:
    #    print("NEW HIGHEST: ", highest)
    #    highest = i
    #print("TYPE: ",type(chain))
    #if i % 1000 == 0:
    #    print("NUMBER: ",i)
    #    print("CHAIN LENGTH: ",chain)
memory = sorted(memory.items(),key=operator.itemgetter(1),reverse=True)
print("MEMORY[0]: ", memory[0])
#print("FINAL HIGHEST : ",highest)