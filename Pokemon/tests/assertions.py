from IPython.display import Image

def stepone(pokemon_name: str) -> None:
    if pokemon_name == "unknown":
        print("Vous avez rentré un index de pokemon inconnu")
        return
    print(f"Vous avez choisi {pokemon_name}")
    if pokemon_name == "Poussacha":
        display(Image(filename="Images/poussacha.jpg"))
    elif pokemon_name == "Chochodile":
        display(Image(filename='Images/chochodile.png'))
    elif pokemon_name == "Coiffeton":
        display(Image(filename='Images/coiffeton.jpg'))
    else:
        print("Vous avez rentré un index de pokemon inconnu")