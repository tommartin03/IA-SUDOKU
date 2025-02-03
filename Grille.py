import random
from Case import Case

class Grille:
    def __init__(self):
        self.grille = [[Case() for _ in range(9)] for _ in range(9)]
        self.generer_puzzle()

    def afficher(self):
        print("   " + " ".join(str(i + 1) for i in range(9)))
        print("  -------------------")
        for i in range(9):
            print(f"{i + 1} |", end="")
            for j in range(9):
                print(f" {self.grille[i][j]}{'|' if (j + 1) % 3 == 0 else ''}", end="")
            print()
            if (i + 1) % 3 == 0:
                print("  -------------------")
        

    def est_valide(self, ligne, colonne, num):
        if num in [self.grille[ligne][j].valeur for j in range(9)]:
            return False
        if num in [self.grille[i][colonne].valeur for i in range(9)]:
            return False
        debut_ligne, debut_colonne = 3 * (ligne // 3), 3 * (colonne // 3)
        for i in range(debut_ligne, debut_ligne + 3):
            for j in range(debut_colonne, debut_colonne + 3):
                if self.grille[i][j].valeur == num:
                    return False
        return True
    
    def remplir_grille(self):
        for i in range(9):
            for j in range(9):
                if self.grille[i][j].valeur == 0:
                    nombres = list(range(1, 10))
                    random.shuffle(nombres)
                    for num in nombres:
                        if self.est_valide(i, j, num):
                            self.grille[i][j].valeur = num
                            if self.remplir_grille():
                                return True
                            self.grille[i][j].valeur = 0
                    return False
        return True

    def generer_puzzle(self):
        self.remplir_grille()
        for _ in range(40): 
            ligne, colonne = random.randint(0, 8), random.randint(0, 8)
            while self.grille[ligne][colonne].valeur == 0:
                ligne, colonne = random.randint(0, 8), random.randint(0, 8)
            self.grille[ligne][colonne].valeur = 0
            self.grille[ligne][colonne].modifiable = True

    def est_complet(self):
        return all(self.grille[i][j].valeur != 0 for i in range(9) for j in range(9))