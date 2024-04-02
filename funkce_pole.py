#Zde si vytváříme pole s prvky, všechny prvky jsou datového typu string
#          0       1       2      3
cars = ["Ford", "Volvo", "BMW", "Audi"]

#Vytvoříme si funkci, která nám vypíše všechny prvky z pole pod sebe
#Funcki si vytváříme proto, abychom nemuseli kód opisovat znova
#Pokud budu chtít vypsat prvky z pole, stačí zavolat tuhle funkci
#Zavoláme jí "vypis_pole(sem zadáte, jaké pole chcete vypsat)"
def vypis_pole(prvek):
    #Ve funkci v závorce je parametr funkce, tu musíme propisovat i do funkce
    #Když zadám parametr funkce příklad: vypi_pole(cars)
    #Změní se prvek na cars v celé funkci

    #Cyklus s pevným počtem opakování
    #x používáme v cyklu, jako čísli cyklu
    #Cyklus proběhne poprvé, x = 0, po druhé x = 1 ...
    #range - pevný počet opakování
    #len(sem zadejte pole/prvek kvuli funkci) - vrátí hodnotu délky pole
    for x in range(len(prvek)):
        #x + 1 - aby nám to vypisovalo pořadí od 1
        #Kdyby to tam nebylo, číslování by bylo od 0, protože cyklus začíná od nuly
        #prvek[x] - podle cyklu vypíše všechny prvky z pole 
        print(f"Auto s číslem {x+1}: {prvek[x]}")
        #Tohle sem dáváme, aby to bylo od sebe nějak oddělený
        print(" ")

#Přidání prvku do pole
        
#Uložím do proměné prvek, která budu chtít přidat
prvek_plus = input("Zadejte auto, které chcete přidat: ")


#Přidání prvku do pole
#Pokud chci něco s polem dělat a používát funkce, musíme zadat název_pole a dát k něm "." a následně funkci
#Funkce append(), můžeme říct, že adoptuje nový prvek a dá ho na konec pole
#Zde efektivně pracujeme s tím, že do parametru appande() dáváme proměnou, do které uživatel uložít hodnotu,
#která se přidá do pole
cars.append(prvek_plus)
#Voláme funkci (kterou jsme si vytvořili na řádku 9), aby mi vypasalo pole cars, cars jsem zadal do parametru funkce 
vypis_pole(cars)


#Odebrat pole podle pozice
#Uložíme si číslo pozice, které budeme chtít z pole odstranit
prvek_minus = int(input("Jakou pozici chcete odebrat? "))

#Funkce pop(), pokud do něj nic nenapíšeme, odstraní poslední prvek v poli
#Pokud bychom zadali cars.pop(0) odstraní prvek na pozici 0.
#Pokud bychom zadali pozici, který v poli není, vyhodí nám error
#Zde efektivně pracujeme i s proměnou, kterou zadá uživatel, uživatel rozhoduje, který prvek se odrstraní

cars.pop(prvek_minus)
#Znovu zavoláme funkci pro výpis pole
vypis_pole(cars)