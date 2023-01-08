import math

list_numbers = [3.5, 6.8, 9.05, 3.009]
list_residue = []
for i in list_numbers:
    list_residue.append(round(i - math.floor(i), 5))
print(f'{list_residue} = > {max(list_residue, default=0) - min(list_residue, default=0)}')