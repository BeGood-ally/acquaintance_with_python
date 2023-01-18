mass = ['U', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'g', 'g', 'g']
mass_arh = ['U1', 'A5', 'B4', 'C2', 'g3']

def archiver(massive):
    massive_arh = []
    temp = massive[0]
    massive_arh.append(f'{massive[0]}{massive.count(massive[0])}')
    for i in massive:
        if i == temp:
            continue
        if i != temp:
            massive_arh.append(f'{i}{massive.count(i)}')
            temp = i
    return massive_arh

def dearchiver(massive):
    massive_dearh = []
    for i in massive:
        for j in range(0, int(i[1])):
            massive_dearh.append(i[0])
    return massive_dearh

print(f'{archiver(mass)}\n{dearchiver(mass_arh)}')