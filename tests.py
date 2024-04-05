zbozi = ["CPU", "GPU", "RAM", "Motherboard", "Zdroj", "Case"]
kosik = []

def vypis_pole(prvek):
    for x in range(len(prvek)):
        print(f"{x+1}. {prvek[x]}")

def kosik_plus(zbozi, index, kosik):
    vyber = zbozi.pop(index)
    kosik.append(vyber)
    print(f"{vyber} byla přidána do košíku")

while True:
    print("Zboží k dispozici: ")
    vypis_pole(zbozi)

    volba = input("Vyberte položku podle čísla nebo zadejte 'konec' pro ukončení nákupu: ")

    if volba == 'konec':
        break

    index = (int(volba) - 1)
    kosik_plus(zbozi, index, kosik) if 0 < index <= len(zbozi) else print("Neplatná volba. Zadejte prosím platné číslo")

print("Vaše položky v košíku: ")
if len(kosik) > 0:
    print(", ".join(kosik))
else:
    print("Košík je prázdný")