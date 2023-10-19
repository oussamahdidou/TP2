direction = input(
    "choisi  le mad => euro ou l`inverse ecrire euro si le 1er cas mad si l`inverse"
)
L = []
a = 10
if direction == "euro":
    while a > 0:
        a = float(input(""))
        L.append(a / 10.86)

elif direction == "mad":
    while a > 0:
        a = float(input(""))
        L.append(a * 10.86)
print(L)
