## Exercices de base

### majeur / mineur
demander l'age de l'utilisateur, retourner s'il est majeur ou mineur

### Plus grand nombre
soit le tableau suivant : 

```python
tab = [2, 7, 93, 45, 2, 129, 403, 5, 894, 345, 209]
```

Afficher le plus grand nombre


### actions bourse
soit le tableau suivant : 

```python
tab = [
    # [nom, prix, rendement]
    ["a", 120, "12%"],
    ["b", 10, "25%"],
    ["c", 26, "44%"],
    ["d", 390, "10%"],
    ["e", 225, "26%"],
    ["f", 89, "38%"],
]
```

Identifier l'action avec le plus de rendement

### actions bourse FONCTION
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

Soit une fonction ```toto()``` qui prend en paramètre une valeur monétaire.
Les rendements sont versés anuellement.
On ne peut acheter qu'une seule action, mais autant de fois qu'on veut.
Calculez, à partir d'un montant donné (le paramètre), l'action la plus rentable à acheter en fonction de votre budget (= le paramètre)