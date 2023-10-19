L = [1, -30, 0, -2, 500, 4, 2, 100]
M = []
for nombre in L:
    if nombre < 0:
        M.append(nombre)
for nombre in L:
    if nombre >= 0:
        M.append(nombre)
print("Liste originale L :", L)
print("Liste modifiée M :", M)
