class Voiture:
    def __init__(self, moteur, roue, carosserie):
        self.moteur = moteur
        self.roue = roue
        self.carosserie = carosserie

    def accept(self, visitor):
        visitor.visitVoiture(self)

class Moteur:
    def __init__(self, cylindre):
        self.nb_cylindre = cylindre

    def accept(self, visitor):
        visitor.visitMoteur(self)

class Roue:
    def __init__(self, roue, jante):
        self.nb_roue = roue
        self.nb_jante = jante

    def accept(self, visitor):
        visitor.visitRoue(self)

class Carosserie:
    def __init__(self, porte):
        self.porte = porte

    def accept(self, visitor):
        visitor.visitCarrosserie(self)

