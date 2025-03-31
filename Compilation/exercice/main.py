import voiture
import visitor as my_visitor


ast = voiture.Voiture(voiture.Moteur(8),
                      voiture.Roue(4,4),
                      voiture.Carosserie(3))

visitor = my_visitor.Visitor()
visitor.visitAst(ast)

