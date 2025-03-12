
import random 

ord_lista = ["blixt", "fängelse", "jordglob", "kaktus", "mysterium", "ostron", "pyttipanna", "spegel", "björklöv", "elgitarr"]


mitt_ord = random.choice(ord_lista)     # Randomly chooses a word from the words list

display = ["_" for _ in mitt_ord]       # Skapar lista med "_"

antal_liv = 8                           # Antal gånger man kan gissa

poäng = 0                               # Antal gånger man gissar rätt irad


print("\nVälkommen till HÄNGAGUBBE!")


while antal_liv > 0 and "_" in display:
    print("\n" + " ".join(display) + "\n")

    gissning = input("Gissa en bokstav:" ).lower()
    
    if gissning in mitt_ord:
        for index, bokstav in enumerate(mitt_ord):
            if bokstav == gissning:
                display[index] = gissning # visa bokstaven
    
    else:
        antal_liv -= 1
        print("\nFel. Bokstaven '"+ gissning.capitalize() +"' finns inte i ordet.")

# Slutet av spelet

if "_" not in display:
    print("\nDu gissa rätt!")
    print("\nOrdet är: " + mitt_ord.capitalize())
    
    print("\n+1 poäng")             #Poäng? hur restartar man??
    poäng += 1 
    print("\nPoäng: ", poäng)
    antal_liv = 8

else:
    print("\n\nDu har slut på gissningar")
    print("\nOrdet var: " + mitt_ord.capitalize())
    print("\nDu blev tyvärr hängd x_x")
    print("\nSlutgiltiga poäng: ", poäng)