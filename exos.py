# Exo 1 : majeur/mineur
# age = input("Ecrivez votre age : ")
# if int(age) > 17:
#     print("Vous êtes majeur")
# else:
#     print("Vous êtes mineur")


# Exo 2 
# tab = [2, 7, 93, 45, 2, 129, 1403, 5, 894, 345, 209]
# max = tab[0]
# for t in tab:
#     if t >= max :
#         max = t
# print("Le max est : ", max)

# Exo 3
tab = [
    # [nom, prix, rendement]
    ["a", 120, "12%"],
    ["b", 10, "25%"],
    ["c", 26, "44%"],
    ["d", 390, "10%"],
    ["e", 225, "26%"],
    ["f", 89, "38%"],
]
rep = tab[0]
for elt in tab:
    if elt[2] > rep[2]:
        rep = elt
print('L\'action avec le plus de rendement est l\'action', rep[0])



# Exo 4
tab = [
    # [nom, prix, rendement]
    ["a", 120, "12%"],
    ["b", 10, "25%"],
    ["c", 26, "44%"],
    ["d", 390, "10%"],
    ["e", 225, "26%"],
    ["f", 89, "38%"],
]

def toto(valeur, tab):
    gainPotentiel = 0
    gainReel = 0
    bestRendement = 0
    bestAction = tab[0]
    for action in tab:
        pourcentage = float(action[2].replace('%', ''))
        gainPotentiel = action[1] * pourcentage / 100
        quotient = valeur // action[1]
        gainReel = quotient * gainPotentiel
        if gainReel > bestRendement:
            bestRendement = gainReel
            bestAction = action
    return [bestRendement, bestAction]

resultat = toto(140, tab)
print('La meilleure action est l\'action', resultat[1][0], 'avec un rendement maximal de', resultat[0], '€')