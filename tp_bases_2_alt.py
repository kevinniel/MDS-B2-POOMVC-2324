class Action:

    def __init__(self, name, price, rendement):
        self.name = name
        self.__price = price
        self.rendement_ratio = float(rendement[:-1]) / 100
        self.rendement_euros = self.__calculer_rendement_annuel()

    # Accesseur || Accessor || Getter
    def get_price(self):
        return self.__price

    # Mutateur || Mutator || Setter
    def set_price(self, price):
        self.price = price
        self.rendement_euros = self.__calculer_rendement_annuel()

    def __calculer_rendement_annuel(self):
        return self.price * self.rendement_ratio

    def calculer_rendement_annuel_max(self, budget):
        nb_actions_achetables = budget // self.price
        return nb_actions_achetables * self.rendement_euros

class Main:

    tab = [
        ["a", 120, "12.3%"],
        ["b", 10, "11.5%"],
        ["c", 26, "10.9%"],
        ["d", 390, "11.8%"],
        ["e", 225, "11.7%"],
        ["f", 89, "12.1%"],
    ]

    def __init__(self):
        self.budget = self.demande_budget()
        self.action_la_plus_rentable()

    def demande_budget(self):
        return int(input("Quel est votre budget :"))

    def action_la_plus_rentable(self):
        meilleure_action = None
        meilleur_rendement = 0

        for info_action in self.tab:
            action = Action(*info_action)
            rendement_annuel = action.calculer_rendement_annuel_max(self.budget)

            if rendement_annuel > meilleur_rendement:
                meilleur_rendement = rendement_annuel
                meilleure_action = action

        if meilleure_action:
            print(f"La meilleure action à acheter est '{meilleure_action.name}' avec un rendement annuel de {meilleur_rendement:.1f} euros.")
        else:
            print("Aucune action n'est disponible avec le budget fourni.")
 
if __name__ == "__main__":
    Main()