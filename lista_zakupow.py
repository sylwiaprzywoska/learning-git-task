print("lista zakupów")
slownik = {"piekarnia": ["chleb", "bułki", "pączek", "jagodzianka"], "warzywniak": ["marchew", "seler", "rukola", "bakłażan"]}
i = 0
j=0
for sklep, item in slownik.items():
    sklep = sklep.capitalize()
    print(f"idę do {sklep} i kupuję: {item}")
    i = len(item)
    j = j + i
print(f"W sumie kupuję {j} produktów")
