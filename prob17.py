import inflect
count = 0
p = inflect.engine()

for i in range(1,1001):
    num = p.number_to_words(i)
    for letter in num:
        if letter == '-' or letter == ' ':
            pass
        else:
            count += 1

print("LETTER COUNT: ",count)