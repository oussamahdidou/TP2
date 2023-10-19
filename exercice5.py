L = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11]
a = int(input("donner un nombre : "))
for i in range(len(L)):
    if L[i] > 8:
        L.insert(i, 8)
        break
print(L)
