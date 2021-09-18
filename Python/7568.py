ln = int(input())
people = []
for i in range(ln):
    people.append([int(i) for i in input().split()])
rank = [1] * ln
for i in range(ln):
    for j in range(ln):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank[i] += 1
print(' '.join([str(i) for i in rank]))
