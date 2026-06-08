word = input()
is_pal = True
for i in range(len(word)//2):
    if word[i] != word[-i-1]:
        is_pal = False
print(1 if is_pal else 0)