from IPython.display import Image
from typing import List

class Pokemon:
    def __init__(self, name, type, level=1, max_health=100,\
        current_health=100, type_force=10, normal_force=6,\
        boost_attack=1, boost_multiplier=2.2, type_multiplier=1.5):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = max_health
        self.current_health = current_health
        self.type_force = type_force
        self.normal_force = normal_force
        self.boost_attack = boost_attack
        self.boost_multiplier = boost_multiplier
        self.type_multiplier = type_multiplier
        self.attacks = ["Charge", "Croissance"]
        if type == "Feu":
            self.attacks.append("Flammeche")
        elif type == "Eau":
            self.attacks.append("Pistolet a O")
        elif type == "Plante":
            self.attacks.append("Tranch'Herbe")
        else:
            self.attacks.append("Special")
    def level_up():
        level += 1
        max_health = max_health * 1.2
        current_health = max_health
        type_force = type_force * 1.2
        normal_force = normal_force * 1.2
        charge = charge * 1.2
        charge_multiplier = charge_multiplier * 1.2
        type_multiplier = type_multiplier * 1.2
    def attack(self, other, attack_name):
        if attack_name == "Charge":
            other.current_health -= self.normal_force * self.boost_attack
        elif attack_name == "Croissance":
            self.charge_multiplier = self.charge_multiplier * 1.5
        elif attack_name == "Pistolet a O" or attack_name == "Hydroblast" or attack_name == "Tranch'Herbe":
            if self.type == "Feu" and other.type == "Plante":
                other.current_health -= self.type_force * self.boost_attack * self.type_multiplier
            elif self.type == "Eau" and other.type == "Feu":
                other.current_health -= self.type_force * self.boost_attack * self.type_multiplier
            elif self.type == "Plante" and other.type == "Eau":
                other.current_health -= self.type_force * self.boost_attack * self.type_multiplier
            else:
                other.current_health -= self.type_force * self.boost_attack
    def reset_boost(self):
        self.boost_attack = 1

def stepone(pokemon_name: str, pokemons: List[Pokemon]) -> None:
    if pokemon_name == "unknown":
        print("Vous avez rentré un index de pokemon inconnu")
        return
    if pokemon_name == "Poussacha":
        display(Image(filename="Images/poussacha.jpg"))
        pokemons.append(Pokemon("Poussacha", "Plante"))
    elif pokemon_name == "Chochodile":
        display(Image(filename='Images/chochodile.png'))
        pokemons.append(Pokemon("Chochodile", "Feu"))
    elif pokemon_name == "Coiffeton":
        display(Image(filename='Images/coiffeton.jpg'))
        pokemons.append(Pokemon("Coiffeton", "Eau"))
    print(f"Vous avez choisi {pokemon_name}")
    print("Voici ses statistiques:")
    print(f"Niveau: {pokemons[0].level}")
    print(f"Type: {pokemons[0].type}")
    print(f"Vie: {pokemons[0].current_health}/{pokemons[0].max_health}")
    print(f"Force: {pokemons[0].normal_force}")
    print(f"Force de type: {pokemons[0].type_force}")
    print(f"Multiplicateur de force: {pokemons[0].boost_multiplier}")
    print(f"Multiplicateur de force de type: {pokemons[0].type_multiplier}")
    print(f"Attaques: {pokemons[0].attacks}")