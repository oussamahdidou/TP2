a = int(input("donner un nombre"))
for i in range(a):
    for j in range(i):
        print("*", end="")
    print()
for i in range(a):
    for j in range(i):
        print(f"{i}", end="")
    print()
