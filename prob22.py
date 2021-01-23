total = 0

with open('p022_names.txt','r') as file:
    data = file.read()
    names = sorted(list(data.lower().replace('"','').split(",")))

for name in names:
    numbers = [ord(letter)-96 for letter in name]
    total += sum(numbers)*(names.index(name)+1)
print("TOTAL: ",total)