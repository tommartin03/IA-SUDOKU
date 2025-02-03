from Grille import Grille

class JeuSudoku:
    def __init__(self):
        self.grille = Grille()

    def jouer(self):
        print("Bienvenue dans le jeu de Sudoku !")
        self.grille.afficher()

        while not self.grille.est_complet():
            try:
                ligne = int(input("Entrez le numéro de ligne (1-9): ")) - 1
                colonne = int(input("Entrez le numéro de colonne (1-9): ")) - 1
                num = int(input("Entrez le nombre (1-9): "))

                if not (0 <= ligne < 9 and 0 <= colonne < 9):
                    print("Ligne ou colonne invalide. Veuillez réessayer.")
                    continue

                case = self.grille.grille[ligne][colonne]
                if not case.modifiable:
                    print("Cette case n'est pas modifiable. Veuillez réessayer.")
                    continue

                if not self.grille.est_valide(ligne, colonne, num):
                    print("Mouvement invalide. Essayez encore.")
                    continue

                case.valeur = num
                self.grille.afficher()

            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre entre 1 et 9.")

        print("Félicitations, vous avez terminé le Sudoku !")