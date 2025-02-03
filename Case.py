class Case:
    def __init__(self, valeur=0):
        self.valeur = valeur
        self.modifiable = valeur == 0

    def __str__(self):
        return str(self.valeur) if self.valeur != 0 else " "