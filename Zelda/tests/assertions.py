import random

from numpy import char

def stepone(destinations):
    print(f"OUTPUT: {destinations}")
    if destinations == ["41.40338, 2.17403", "57.73924, 9.04920"]:
        print("Step 1: Pass\n")
        print(f"Temple de Ma'Ohnu: X = 41.40338, Y = 2.17403")
        print(f"Temple de Shao'Yo: X = 57.73924, Y = 9.04920")
    else:
        print("Step 1: Fail")

def steptwo(code):
    print(f"OUTPUT: {code}")
    if code == 6402:
        print("Step 2: Pass\n")
        print("La porte s'ouvre.")
    else:
        print("Step 2: Fail")

def stepthree(plateforme):
    res = [
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    ]
    print(f"OUTPUT:")
    for row in plateforme:
        print(f"{row}")
    if plateforme == res:
        print("Step 3: Pass\n")
        print("Une porte cachée se dérobe.")
    else:
        print("Step 3: Fail")

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
        print("Vous entrez dans la Foret Korogu.")
    else:
        print("Step 4: Fail")

def fight(makeAction):
    attack = "attack"
    dodge = "dodge"
    counter = "counter"
    charge = "charge" # <-- Only for Ganon's patterns
    sleep = "sleep"
    ganonLife = 3
    linkLife = 1
    GanonPatterns = []
    LinkPatterns = []
    ganonActions = ["attack", "charge"]
    while (linkLife > 0 and ganonLife > 0):
        print(f"\nVie de Link: {linkLife} | Vie de Ganon: {ganonLife}\t->\t", end="")

        #Append Ganon action
        if len(GanonPatterns) > 1 and GanonPatterns[-1] == attack and GanonPatterns[-2] == attack:
            GanonPatterns.append(sleep)
        elif len(GanonPatterns) > 0 and GanonPatterns[-1] != charge:
            GanonPatterns.append(random.choice(ganonActions))
        else:
            GanonPatterns.append("attack")

        #Append Link action
        if len(GanonPatterns) < 1 and len(LinkPatterns) < 0 and GanonPatterns[-2] != attack and LinkPatterns[-1] == dodge:
            LinkPatterns.append(sleep)
        else:
            LinkPatterns.append(makeAction(GanonPatterns[:-1], LinkPatterns))

        # Turn ganon's action
        if GanonPatterns[-1] == attack:
            print("Ganon attaque.", end=" ")
        elif GanonPatterns[-1] == charge:
            print("Ganon charge. ", end=" ")
        elif GanonPatterns[-1] == sleep:
            print("Ganon dort.", end=" ")

        # Turn link's action
        if LinkPatterns[-1] == attack:
            print("Link attaque.", end=" ")
            print("Ganon prend des dégats.", end=" ")
            ganonLife = ganonLife - 1
            if len(GanonPatterns) > 1 and GanonPatterns[-1] == attack and GanonPatterns[-2] == charge:
                print("Link prend des dégats.", end=" ")
                linkLife = linkLife - 3
            elif GanonPatterns[-1] == attack:
                print("Link prend des dégats.", end=" ")
                linkLife = linkLife - 1
        elif LinkPatterns[-1] == dodge:
            if (GanonPatterns[-1] != attack):
                print("Link esquive.", end=" ")
            else:
                if (len(GanonPatterns) > 1 and GanonPatterns[-2] != charge)  or len(GanonPatterns) < 2:
                    print("Link esquive.", end=" ")
                else:
                    linkLife = linkLife - 3
                    print("Link prend des dégats.", end=" ")
        elif LinkPatterns[-1] == counter:
            if (GanonPatterns[-1] != attack):
                print("Link contre.", end=" ")
            else:
                if len(GanonPatterns) > 1 and GanonPatterns[-2] == charge:
                    print("Link contre.", end=" ")
                else:
                    linkLife = linkLife - 3
                    print("Link prend des dégats.", end=" ")
        elif LinkPatterns[-1] == sleep:
            print("Link dort.", end=" ")
            if len(GanonPatterns) > 1 and GanonPatterns[-1] == attack and GanonPatterns[-2] == charge:
                print("Link prend des dégats.", end=" ")
                linkLife = linkLife - 3
            elif GanonPatterns[-1] == attack:
                print("Link prend des dégats.", end=" ")
                linkLife = linkLife - 1
        else:
            print("Link ne fait rien.", end=" ")
            if len(GanonPatterns) > 1 and GanonPatterns[-1] == attack and GanonPatterns[-2] == charge:
                print("Link prend des dégats.", end=" ")
                linkLife = linkLife - 3
            elif GanonPatterns[-1] == attack:
                print("Link prend des dégats.", end=" ")
                linkLife = linkLife - 1

    # end
    if (linkLife <= 0):
        print("\n\nVous avez perdu !")
        if ganonLife > 1:
            print(f"il reste {ganonLife} vies à Ganon.")
        else:
            print(f"il reste {ganonLife} vie à Ganon.")
    else:
        print("\n\nVous avez vaincu Ganon !")
        if linkLife > 1:
            print(f"Il vous reste {linkLife} vies.")
        else:
            print(f"il vous reste {linkLife} vie.")
