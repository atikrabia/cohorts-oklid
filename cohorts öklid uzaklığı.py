import math

# 1. Noktaların Tanımlanması
noktalar = [(1, 2), (3, 4), (6, 8), (9, 10), (2, 3)]

# 2. Öklid Mesafesi İçin Bir Fonksiyon Yazma
def oklidMesafesi(nokta1, nokta2):
    return math.sqrt((nokta2[0] - nokta1[0]) ** 2 + (nokta2[1] - nokta1[1]) ** 2)

# 3. Mesafelerin Hesaplanması
mesafeler = []
for i in range(len(noktalar)):
    for j in range(i + 1, len(noktalar)):
        mesafe = oklidMesafesi(noktalar[i], noktalar[j])
        mesafeler.append(mesafe)

# 4. Minimum Mesafenin Bulunması
min_mesafe = min(mesafeler)

# Sonuçların Yazdırılması
print(f"Noktalar: {noktalar}")
print(f"Mesafeler: {mesafeler}")
print(f"Minimum Mesafe: {min_mesafe}")
#açıklama