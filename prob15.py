size = 20
paths = 1
for i in range(size):
    paths *= (2*size)-i
    paths /= i + 1
print("PATHS: ",int(paths))