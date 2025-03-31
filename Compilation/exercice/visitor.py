class Visitor:
    def visitAst(self, ast):
        ast.accept(self)

    def visitVoiture(self, voiture):
        voiture.moteur.accept(self)
        voiture.roue.accept(self)
        voiture.carosserie.accept(self)

    def visitMoteur(self, moteur):
        #moteur.nb_cylindre.accept(self)
        print("Cylindre", moteur.nb_cylindre)

    def visitCarrosserie(self, carrosserie):
        #carrosserie.porte.accept(self)
        print("Porte", carrosserie.porte)

    def visitRoue(self, roue):
        #roue.nb_roue.accept(self)
        #roue.nb_jante.accept(self)
        print("Nombre de roue : ", roue.nb_roue)
        print("Nombre de jante : ", roue.nb_jante)

