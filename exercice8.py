a = int(input("donner un nombre : "))
nmbr_occurence = 0
L = [1, 2, 5, 8, 6, 2, 5, 9, 1, 8, 8]
positions = []
for i in range(len(L)):
    if L[i] == a:
        nmbr_occurence += 1
        positions.append(i)
print(
    f"le nombre {a} est apparue {nmbr_occurence} fois dans les positions suivantes {positions}"
)
