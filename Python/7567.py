plate = input()
diff = 1
for i in range(1, len(plate)):
    diff += plate[i] != plate[i-1]
print(len(plate)*5 + diff*5)