# TP bases POO
Créez un programme qui permet de jouer avec des dés, d'effectuer un lancer (de 2 dés) et de ressortir les informations suivantes sur chaque lancé : 
- valeur dé 1
- valeur dé 2
- est-ce un double ?
- somme des deux dés
- produit des deux dés

Votre code ne doit contenir QUE de la POO, aucune PP autorisée

# TP bases 2 POO

soit le tableau suivant : 

```python
tab = [
    # [nom, prix, rendement]
    ["a", 120, "12.3%"],
    ["b", 10, "11.5%"],
    ["c", 26, "10.9%"],
    ["d", 390, "11.8%"],
    ["e", 225, "11.7%"],
    ["f", 89, "12.1%"],
]
```

Créer une classe Action qui gère l'ensemble des actions ci-dessus.
Trouver l'action qui à le meilleur rendement à partir d'un montant disponible.
Les rendements sont versés anuellement.
On ne peut acheter qu'une seule action, mais autant de fois qu'on veut.

!!! Calculez, à partir d'un montant donné (le paramètre), l'action la plus rentable à acheter en fonction de votre budget (= le paramètre) ===> dans une classe "Main"



# TP MVC POO
Réalisez un programme permettant de scrapper les informations d'une bibliothèque sur le site https://books.toscrape.com/

## Étape 1
Vous devez être capable de récupérer toutes les informations possibles sur un livre (prix, info, description, url image, etc...)

## Étape 2
gérer la même chose sur un nombre illimité d'URL => vous devez automatiser la récupération de toutes les URLs pour une catégorie donnée

## Étape 3
Sauvegarder toutes les informations en BDD

## Étape 4
Mise en place d'une architecture MVC