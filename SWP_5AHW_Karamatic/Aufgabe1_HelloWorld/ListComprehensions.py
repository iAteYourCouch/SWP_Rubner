list = [-2, -3, -1, 0, 1, 2, 3, 4, 5, 6, 8, 12, 13]

#positive zahlen
posZahlen = [x for x in list if x > 0]
print(posZahlen)

rang = [x for x in range(-4, 12) if x % 2 == 1]
print(rang)

negZahl = [y for y in range(-20, 10) if y < 0 and y % 4 == 3]
print(negZahl)

squa = [(x, x**2) for x in list if x%2 == 1]
print(squa)

straight = [x for x in list if x % 2 == 0]
print(straight)

strings = ["Gerade" if x % 2 == 0 else "Ungerade" for x in list]
print(strings)

back = list[::-1]
print(back)
print(sorted(list, reverse=True))
