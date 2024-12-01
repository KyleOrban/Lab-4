firstpoints = 10
totalpoints = firstpoints
backpack = []
allweight = 0
maxsize = 9

items = [
    ('r', 3, 25),
    ('p', 2, 15),
    ('a', 2, 15),
    ('m', 2, 20),
    ('i', 1, 5),
    ('k', 1, 15),
    ('x', 3, 20),
    ('t', 1, 25),
    ('f', 1, 15),
    ('d', 1, 10),
    ('s', 2, 20),
    ('c', 2, 20)
]

backpack.append(items[4])
items.pop(4)

sortitems = sorted(items, key = lambda x: (x[1], -x[2]))




for item in sortitems:
    if allweight+item[1] <= maxsize:
        backpack.append(item)
        allweight+=item[1]
        totalpoints+=item[2]
    else:
        totalpoints-=item[2]


inventory = [['empty' for _ in range(3)] for _ in range(3)]

for j in range(len(backpack)):
    x = j//3
    y = j%3
    inventory[x][y]=backpack[j][0]
    inventory[2][0]=backpack[5][0]
    inventory[2][1]=backpack[6][0]
    inventory[2][2]=backpack[6][0]


print("Решение для 3x3 инвентаря:")
if totalpoints > 0:
    print('Инвентарь:')
    for row in inventory:
        print(row[0], row[1], row[2],)
    print(f'Очки: {totalpoints}')
else:
    print('Решений нет!')

print("  ")
print("  ")
print("  ")


firstpoints = 10
totalpoints = firstpoints
backpack = []
allweight = 0
maxsize = 7

items = [
    ('r', 3, 25),
    ('p', 2, 15),
    ('a', 2, 15),
    ('m', 2, 20),
    ('i', 1, 5),
    ('k', 1, 15),
    ('x', 3, 20),
    ('t', 1, 25),
    ('f', 1, 15),
    ('d', 1, 10),
    ('s', 2, 20),
    ('c', 2, 20)
]

backpack.append(items[4])
items.pop(4)

sortitems = sorted(items, key = lambda x: (x[1], -x[2]))




for item in sortitems:
    if allweight+item[1] <= maxsize:
        backpack.append(item)
        allweight+=item[1]
        totalpoints+=item[2]
    else:
        totalpoints-=item[2]


inventory = ['empty' for _ in range(7)]

for j in range(len(backpack)):
    inventory[j] = backpack[j]

print("Решение для 7x1 инвентаря:")
if totalpoints > 0:
    print('Инвентарь:')
    for row in inventory:
        print(row[0], row[1], row[2],)
    print(f'Очки: {totalpoints}')
else:
    print('Решений нет!')