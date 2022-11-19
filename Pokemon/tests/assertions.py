from IPython.display import Image, HTML
from typing import List
from random import choice, randint


class Pokemon:
    def __init__(
        self,
        name: str,
        type: str,
        level: int = 1,
        max_health: int = 100,
        current_health: int = 100,
        attack: int = 10,
        boost_attack: int =1,
        boost_multiplier: float = 2.2,
        type_multiplier: float = 1.5
    ):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = max_health
        self.current_health = current_health
        self.attack = attack
        self.boost_attack = boost_attack
        self.attacks: List[str] = ["Charge", "Croissance"]
        if type == "Feu":
            self.attacks.append("Flammeche")
        elif type == "Eau":
            self.attacks.append("Pistolet a O")
        elif type == "Plante":
            self.attacks.append("Tranch'Herbe")
        else:
            self.attacks.append("Special")
        while len(self.attacks) < 4:
            self.attacks.append("None")

    def level_up(self):
        self.level += 1
        self.max_health = self.max_health * 1.2
        self.current_health = self.max_health
        self.attack = self.attack * 1.2

    def reset_boost(self):
        self.boost_attack = 1

def make_attack(pokemon: Pokemon, other: Pokemon, attack_name: str) -> None:
    if attack_name == "Charge":
        other.current_health -= pokemon.attack * pokemon.boost_attack
    elif attack_name == "Croissance":
        pokemon.boost_attack = pokemon.boost_attack * 1.3
        print(f"{pokemon.name} a maintenant un boost de {pokemon.boost_attack}")
    elif (
        attack_name == "Pistolet a O"
        or attack_name == "Flammeche"
        or attack_name == "Tranch'Herbe"
    ):
        if pokemon.type == "Feu" and other.type == "Plante":
            other.current_health -= pokemon.attack * pokemon.boost_attack * 1.5
            print(f"{pokemon.name} à infligé {pokemon.attack * pokemon.boost_attack * 1.5} dégats à {other.name}")
        elif pokemon.type == "Eau" and other.type == "Feu":
            other.current_health -= pokemon.attack * pokemon.boost_attack * 1.5
            print(f"{pokemon.name} à infligé {pokemon.attack * pokemon.boost_attack * 1.5} dégats à {other.name}")
        elif pokemon.type == "Plante" and other.type == "Eau":
            other.current_health -= pokemon.attack * pokemon.boost_attack * 1.5
            print(f"{pokemon.name} à infligé {pokemon.attack * pokemon.boost_attack * 1.5} dégats à {other.name}")
        else:
            other.current_health -= pokemon.attack * pokemon.boost_attack
            print(f"{pokemon.name} à infligé {pokemon.attack * pokemon.boost_attack} dégats à {other.name}")
    if other.current_health < 0:
        other.current_health = 0


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
    listOpponents = [heliatron, Aquali, Caninos]
    opponent = listOpponents[randint(0, 2)]
    print(opponent.attacks[0])
    tour = 1

    print(f"Vous avez rencontré un {opponent.name} sauvage !")
    while True:
        action = ""
        print("Que voulez-vous faire ?")
        print("1. changer")
        print("2. potion")
        print("3. pokeball")
        print("4. inventaire")
        i = 5
        for attack in dresseur.current_pokemon.attacks:
            print(f"{i}: {attack}")
            i += 1
        print(f"-----------------|Tour: {tour}|-----------------")
        index_str = input("Entrez le numéro de l'action que vous voulez faire: ")
        action: str = dresseur_actions(index_str)
        if action == "changer":
            i = 1
            for pokemon in dresseur.pokemons:
                if pokemon.current_health > 0 and pokemon != dresseur.current_pokemon:
                    print(f"{i}: {pokemon.name}")
                    i += 1
            if i == 1:
                print("Vous ne pouvez pas changer de pokemon !")
            print(f"-----------------|  FIN  |-----------------")
            tour += 1
        elif action == "potion":
            dresseur.heal_pokemon()
            print(f"Vous avez utilisé une potion")
            print(
                f"{dresseur.current_pokemon.name} a maintenant {dresseur.current_pokemon.current_health} points de vie"
            )
            print(f"-----------------|  FIN  |-----------------")
            tour += 1
        elif action == "pokeball":
            dresseur.catch_pokemon(opponent)
            if opponent in dresseur.pokemons:
                print(f"-----------------|  FIN  |-----------------")
                return 0
            print(f"-----------------|  FIN  |-----------------")
            tour += 1
        elif action == "inventaire":
            dresseur.sac.show_inventory()
            print(f"-----------------|  FIN  |-----------------")
        elif action is not None:
            print(f"{dresseur.current_pokemon.name} utilise {action}")
            make_attack(dresseur.current_pokemon, opponent, action)
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
            print(f"Mauvais choix !")
            continue
        opponent_attack: str = opponent.attacks[randint(0, 2)]
        print(f"{opponent.name} sauvage utilise {opponent_attack}")
        make_attack(opponent, dresseur.current_pokemon, opponent_attack)
        print(f"| {dresseur.current_pokemon.name} | : {dresseur.current_pokemon.current_health} PV")
        print(f"| {opponent.name} | : {opponent.current_health} PV")
        if dresseur.current_pokemon.current_health <= 0:
            print(f"Votre {dresseur.current_pokemon.name} est KO !")
            print(f"Vous avez perdu face au {opponent.name} sauvage")
            print(f"-----------------|  FIN  |-----------------")
            return 2
        tour += 1
        print(f"-----------------|  FIN  |-----------------")
    return 0


def stepfour(path):
    print(f"OUTPUT:\n{path}")
    res = [
        'bas', 'droite', 'droite', 'droite',
        'bas', 'bas', 'droite', 'droite',
        'droite', 'haut', 'haut', 'droite',
        'droite', 'bas', 'bas', 'droite',
        'bas', 'bas', 'gauche', 'bas',
        'bas', 'bas', 'gauche', 'gauche',
        'bas', 'gauche', 'gauche', 'haut',
        'haut', 'gauche', 'gauche', 'bas',
        'gauche', 'gauche', 'haut', 'haut',
        'haut', 'droite', 'droite', 'droite',
        'droite', 'droite'
    ]
    if path == res:
        print("Step 4: Pass\n")
        print("Vous avez réussi à vous rendre à la ville de Pallet !")
    else:
        print("Vous vous éloignez beaucoup trop de la route, vous décidé de revenir sur vos pas.")