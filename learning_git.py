print("Learning Git")

lista_zakupow = {
    "piekarnia": ["chleb","bulki","paczki"],
    "warzywniak": ["marchew","seler","rukola"]
}

count = 0

for key, value in lista_zakupow.items():
    capitalized_values = [item.capitalize() for item in value]
    count = count + len(value) 
    print(f"Ide do {key.capitalize()}, kupuje tu nastepujace rzeczy {capitalized_values}.")
    
print(f"W sumie kupuje {count} produktow.")


"""
Zdefiniuj słownik zawierający listę zakupów, gdzie kluczem jest nazwa sklepu, a wartością lista przedmiotów, które chcesz kupić w danym sklepie.
Następnie za pomocą pętli for, przeiteruj po tym słowniku i wyświetl napis w postaci: Idę do <nazwa sklepu> i kupuję tam <lista produktów>.
Dodatkowo, używając wbudowanych metod operacji na napisach, spowoduj, aby nazwy sklepów i towarów były wypisane wielką literą.
Na koniec, w ostatniej linii wypisz W sumie kupuję <X> produktów.X to sumaryczna liczba towarów, które są na listach.

"""
