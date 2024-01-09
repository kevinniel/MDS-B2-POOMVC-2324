import random
class Dice:
    nb_face = 6
    value = None
    def __init__(self):
        self.launch()
    def launch(self):
        self.value = random.randint(1, self.nb_face)
class Dices:
    dice_1 = Dice()
    dice_2 = Dice()
    def launch(self):
        self.dice_1.launch()
        self.dice_2.launch()
    def get_sum(self):
        return self.dice_1.value + self.dice_2.value
    def get_product(self):
        return self.dice_1.value * self.dice_2.value
    def is_double(self):
        if self.dice_1.value == self.dice_2.value:
            return True
        return False