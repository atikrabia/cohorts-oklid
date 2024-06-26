import math


noktalar = [(1, 2), (3, 4), (6, 8), (9, 10), (2, 3)]


def oklidMesafesi(nokta1, nokta2):
    return math.sqrt((nokta2[0] - nokta1[0]) ** 2 + (nokta2[1] - nokta1[1]) ** 2)


mesafeler = []
for i in range(len(noktalar)):
    for j in range(i + 1, len(noktalar)):
        mesafe = oklidMesafesi(noktalar[i], noktalar[j])
        mesafeler.append(mesafe)


min_mesafe = min(mesafeler)


print(f"Noktalar: {noktalar}")
print(f"Mesafeler: {mesafeler}")
print(f"Minimum Mesafe: {min_mesafe}")
