zbozi = ["CPU", "GPU", "RAM", "Motherboard", "Zdroj", "Case"]
kosik = []

def vypis_pole(prvek):
    for i in range(len(prvek)):
        print(f"{i+1}. {prvek[i]}")

def pridej_do_kosiku(zbozi, index, kosik):
    if 0 <= index < len(zbozi):
        vybrana_položka = zbozi.pop(index)
        kosik.append(vybrana_položka)
        print(f"{vybrana_položka} byla přidána do košíku")
    else:
        print("Neplatná volba. Zadejte prosím platné číslo")

while True:
    print("Zboží k dispozici: ")
    vypis_pole(zbozi)

    volba = input("Vyberte položku podle čísla nebo zadejte 'konec' pro ukončení nákupu: ")

    if volba == 'konec':
        break

    index = int(volba) - 1
    pridej_do_kosiku(zbozi, index, kosik) if 0 <= index < len(zbozi) else print("Neplatná volba. Zadejte prosím platné číslo.")

print("Vaše položky v košíku: ")
if len(kosik) > 0:
    print(" ".join(kosik))
else:
    print("Košík je prázdný")