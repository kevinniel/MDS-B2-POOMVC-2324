# class = Plan
class Voiture:
    
    # attribut => attachés à la Classe, et pas aux objets
    # on parle d'un attribut de classe
    prix = 1000

    # méthodes
    def __init__(self, marque = "citroen"):
        self.marque = marque
        # attributs => attributs d'objet
        marque = "citroen"

    # méthode d'objet
    def get_marque(self):
        return self.marque
    
    # méthode de classe
    @classmethod
    def toto(cls):
        print("toto")
        print(cls.prix)
        print("toto")

    # méthodes statiques
    @staticmethod
    def tata():
        print("tata")


# instanciation de la classe Voiture
# ce qui crée un objet de type Voiture
# et qui le stock dans la variable "voiture_1"
voiture_1 = Voiture()

# 2eme instanciation de la classe Voiture
# création d'un deuxième objet de type Voiture,
# Stocké dans la variable "voiture_2"
voiture_2 = Voiture("renault")


# print(voiture_1.marque)
# print(Voiture.marque)

# voiture_1.toto()
Voiture.toto()
Voiture.tata()