a = int(input("donner un nombre : "))
L = [1, 2, 5, 8, 6, 2, 5, 9, 1, 8, 8]
L = [n for n in L if n != a]
print(L)
