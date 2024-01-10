class Carre:

    toto = 3

    def __init__(self, longueur_cote = 10, nb_cote = 4):
        # attribut publique => pas de _
        # accessible de partout
        self.name = self.__class__.__name__
        # attribut protégé => 1 seul _
        # accessible dans la classe ET dans les classes enfant
        self._nb_cote = nb_cote
        # attribut privé => 2 _
        # ne peut être utilisé que à l'intérieur de la classe
        self.__longueur_cote = longueur_cote
    
    # méthode public
    def perimetre(self):
        return self._nb_cote * self.__longueur_cote

    # méthode protégée
    def _aire(self):
        return self.__longueur_cote ** 2

    # méthode privée
    def __volume(self):
        return self.__longueur_cote ** 3

# Classe Rectangle HERITE de la classe Carre
# => tout ce qui est public dans carre, devient accessible dans rectangle
class Rectangle(Carre):
    def __init__(self, p_longueur_cote = 10, g_longueur_cote = 10, nb_cote = 4):
        # déclenche la méthode init de la classe parent
        super().__init__()
        self.p_longueur_cote = p_longueur_cote
        self.g_longueur_cote = g_longueur_cote

    # on redéfinit la fonction perimetre (qui est déjà définie dans la classe parente)
    # parce que la manière de réaliser le calcul est différent
    # On parle ici de SURCHARGE de méthode
    def perimetre(self):
        return (self.p_longueur_cote + self.g_longueur_cote) * 2
    
    def aire(self):
        return self.p_longueur_cote * self.g_longueur_cote
    def volume(self):
        return None


if __name__ == "__main__":
    c = Carre()
    r = Rectangle()

    print(c.toto)
    print(r.toto)