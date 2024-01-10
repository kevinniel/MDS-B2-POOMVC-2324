# Welcome to POO

# Plan de mes objets Chaise
class Chaise:
    # variables dans un contexte objet s'appellent des ATTRIBUTS
    nb_pied = 4
    couleur = "rouge"
    etat = True # Trou || false

    # fonctions dans un contexte objet s'appellent des METHODES
    def changer_etat(self):
        if self.etat:
            self.etat = False
        else:
            self.etat = True

    def nvl_etat(self, etat):
        self.etat = etat

    # méthodes spéciales (PHP = Méthodes magiques)
    def __repr__(self):
        return "Ceci est un objet Chaise, qui dispose de " + str(self.nb_pied) + " pieds"
    
    # constructeur : se déclenche automatiquement & obligatoirement à la création de l'objet
    # php équivalent : __construct()
    def __init__(self, nb_pied):
        self.nb_pied = nb_pied
        print("coucou je suis une chaise")


# créer une chaise (= créer un objet)
chaise = Chaise(6)
print(chaise)
print(chaise.nb_pied)
print(chaise.couleur)

print(chaise.etat)
chaise.changer_etat()
print(chaise.etat)
chaise.nvl_etat(True)
print(chaise.etat)



