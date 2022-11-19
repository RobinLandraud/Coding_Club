from IPython.display import Image, HTML
from typing import List
from random import choice, randint


class Pokemon:
    def __init__(
        self,
        name,
        type,
        level=1,
        max_health=100,
        current_health=100,
        attack=10,
        boost_attack=1,
        boost_multiplier=2.2,
        type_multiplier=1.5,
    ):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = max_health
        self.current_health = current_health
        self.attack = attack
        self.boost_attack = boost_attack
        self.attacks = ["Charge", "Croissance"]
        if type == "Feu":
            self.attacks.append("Flammeche")
        elif type == "Eau":
            self.attacks.append("Pistolet a O")
        elif type == "Plante":
            self.attacks.append("Tranch'Herbe")
        else:
            self.attacks.append("Special")

    def level_up(self):
        self.level += 1
        self.max_health = self.max_health * 1.2
        self.current_health = self.max_health
        self.attack = self.attack * 1.2

    def attack(self, other, attack_name):
        if attack_name == "Charge":
            other.current_health -= self.attack * self.boost_attack
        elif attack_name == "Croissance":
            self.boost_attack = self.boost_attack * 1.5
        elif (
            attack_name == "Pistolet a O"
            or attack_name == "Flammeche"
            or attack_name == "Tranch'Herbe"
        ):
            if self.type == "Feu" and other.type == "Plante":
                other.current_health -= self.attack * self.boost_attack * 1.5
            elif self.type == "Eau" and other.type == "Feu":
                other.current_health -= self.attack * self.boost_attack * 1.5
            elif self.type == "Plante" and other.type == "Eau":
                other.current_health -= self.attack * self.boost_attack * 1.5
            else:
                other.current_health -= self.attack * self.boost_attack

    def reset_boost(self):
        self.boost_attack = 1


class Sac:
    def __init__(self, pokeballs=5, potions=5):
        self.pokeballs = pokeballs
        self.potions = potions

    def add_pokeball(self, number: int):
        self.pokeballs += number

    def add_potion(self, number: int):
        self.potions += number

    def use_pokeball(self):
        self.pokeballs -= 1

    def use_potion(self):
        self.potions -= 1

    def show_inventory(self):
        print(
            f"Vous avez [{self.pokeballs}] pokeballs et [{self.potions}] potions dans votre sac."
        )


class Dresseur:
    def __init__(self, name: str, pokemons: List[Pokemon], sac: Sac):
        self.name = name
        self.pokemons = pokemons
        self.current_pokemon = pokemons[0]
        self.sac = sac

    def add_pokemon(self, pokemon: Pokemon):
        self.pokemons.append(pokemon)

    def change_pokemon(self, pokemon_name: str):
        for pokemon in self.pokemons:
            if pokemon.name == pokemon_name and pokemon.current_health > 0:
                self.current_pokemon = pokemon

    def heal_pokemon(self):
        if (
            self.current_pokemon.current_health < self.current_pokemon.max_health
            and self.sac.potions > 0
        ):
            self.sac.use_potion()
            self.current_pokemon.current_health += 20
            if self.current_pokemon.current_health > self.current_pokemon.max_health:
                self.current_pokemon.current_health = self.current_pokemon.max_health

    def catch_pokemon(self, pokemon: Pokemon):
        if self.sac.pokeballs > 0:
            self.sac.use_pokeball()
            if pokemon.current_health < pokemon.max_health * 0.15:
                self.add_pokemon(pokemon)
                print(f"Vous avez attrapé {pokemon.name} !")
            elif randint(1, 3) == 1:
                print(f"Vous avez attrapé {pokemon.name} !")
                self.add_pokemon(pokemon)
            else:
                print(f"Ah ! presque... la prochaine fois sera la bonne !")
        else:
            print("Vous n'avez plus de pokeballs !")


def stepone(pokemon_name: str, pokemons: List[Pokemon]) -> None:
    pokemons.clear()
    if pokemon_name == "unknown":
        print("Vous avez rentré un index de pokemon inconnu")
        return
    if pokemon_name == "Poussacha":
        display(Image(filename="Images/poussacha.jpg"))
        pokemons.append(Pokemon("Poussacha", "Plante"))
    elif pokemon_name == "Chochodile":
        display(Image(filename="Images/chochodile.png"))
        pokemons.append(Pokemon("Chochodile", "Feu"))
    elif pokemon_name == "Coiffeton":
        display(Image(filename="Images/coiffeton.jpg"))
        pokemons.append(Pokemon("Coiffeton", "Eau"))
    print(f"Vous avez choisi {pokemon_name}")
    print("Voici ses statistiques:")
    print(f"Niveau: {pokemons[0].level}")
    print(f"Type: {pokemons[0].type}")
    print(f"Vie: {pokemons[0].current_health}/{pokemons[0].max_health}")
    print(f"Force: {pokemons[0].attack}")
    print(f"Attaques: {pokemons[0].attacks}")


def steptwo1(sac: Sac):
    if sac.pokeballs != 5 or sac.potions != 5:
        print("Vous n'avez pas ajoutés les bonnes quantités de pokeballs et de potions")
        sac = Sac(0, 0)
    print(
        f"Vous avez désormais {sac.pokeballs} pokeballs et {sac.potions} potions dans votre sac"
    )


def steptwo2(dresseur: Dresseur, pokemons: List[Pokemon], sac: Sac):
    if dresseur.pokemons == pokemons and dresseur.sac == sac:
        print("Brovo ! Vous avez réussi à créer votre dresseur !")
        print(f"Vous avez choisi {dresseur.name} comme nom de dresseur")
        print(f"Vous avez choisi {pokemons[0].name} comme pokemon de départ")
        print(
            f"Vous avez {sac.pokeballs} pokeballs et {sac.potions} potions dans votre sac"
        )
        print("Vous pouvez maintenant commencer à jouer !")
    else:
        print("Vous n'avez pas réussi à créer votre dresseur !")
        print("Veuillez recommencer")
        dresseur.sac = Sac(0, 0)
        dresseur.pokemons.clear()


def stepthree(dresseur: Dresseur, dresseur_actions) -> int:
    heliatron = Pokemon("Heliatron", "Plante")
    Aquali = Pokemon("Aquali", "Eau")
    Caninos = Pokemon("Caninos", "Feu")
    opponent = choice([heliatron, Aquali, Caninos])
    tour = 1

    print(f"Vous avez rencontré un {opponent.name} sauvage !")
    while True:
        action = ""
        print("Que voulez-vous faire ?")
        print("1. changer")
        print("2. potion")
        print("3. pokeball")
        print("4. inventaire")
        print("5. attaquer:attaque")
        print(f"-----------------|Tour: {tour}|-----------------")
        action = dresseur_actions(input())
        if action == "changer":
            print(f"Vous ne pouvez pas changer de pokemon pour le moment")
            print(f"-----------------|  FIN  |-----------------")
            continue
        elif action == "potion":
            dresseur.heal_pokemon()
            print(f"Vous avez utilisé une potion")
            print(
                f"{dresseur.current_pokemon.name} a maintenant {dresseur.current_pokemon.current_health} points de vie"
            )
            print(f"-----------------|  FIN  |-----------------")
            tour += 1
            continue
        elif action == "pokeball":
            dresseur.catch_pokemon(opponent)
            if opponent in dresseur.pokemons:
                print(f"-----------------|  FIN  |-----------------")
                return 0
            print(f"-----------------|  FIN  |-----------------")
        elif action == "inventaire":
            dresseur.sac.show_inventory()
            print(f"-----------------|  FIN  |-----------------")
            tour += 1
            continue
        elif "Attaque:" in action:
            attack = action.split(":")[1]
            print(f"{dresseur.current_pokemon.name} utilise {attack}")
            dresseur.current_pokemon.attack(opponent, attack)
            if opponent.current_health <= 0:
                print(f"Le {opponent.name} sauvage est KO !")
                print(f"Vous avez échoué à capturer le {opponent.name} sauvage")
                print(f"-----------------|  FIN  |-----------------")
                return 1
            elif dresseur.current_pokemon.current_health <= 0:
                print(f"Votre {dresseur.current_pokemon.name} est KO !")
                print(f"Vous avez perdu face au {opponent.name} sauvage")
                print(f"-----------------|  FIN  |-----------------")
                return 2
        elif action == "None":
            print(f"-----------------|  FIN  |-----------------")
            continue
        opponent_attack = choice(opponent.attacks)
        opponent.attack(dresseur.current_pokemon, opponent_attack)
        if dresseur.current_pokemon.current_health <= 0:
            print(f"Votre {dresseur.current_pokemon.name} est KO !")
            print(f"Vous avez perdu face au {opponent.name} sauvage")
            print(f"-----------------|  FIN  |-----------------")
            return 2
        tour += 1
        print(f"-----------------|  FIN  |-----------------")
    return 0