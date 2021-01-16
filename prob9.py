
def check_triple(a,b,c):
    if a**2 + b**2 == c**2:
        print("PYTHAGOREAN TRIPLE: ", a,b,c)
        print("PRODUCT = ",get_product(a,b,c))

def get_product(a,b,c):
    return a*b*c

for a in range(998):
    for b in range(998):
        for c in range(998):
            if a+b+c == 1000:
                check_triple(a,b,c)