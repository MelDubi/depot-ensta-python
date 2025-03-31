class Program:
    def __init__(self):
        self.declarations = []
        self.statements = []

    def accept(self, visitor):
        visitor.visitProgram(self)

class Declaration:
    def __init__(self, type, identifier, integer=None):
        self.type = type
        self.identifier = identifier
        self.integer = integer

    def accept(self, visitor):
        visitor.visitDeclaration(self)

class Body:
    def __init__(self):
        self.body = []

    def accept(self, visitor):
        visitor.visitBody(self)

class Statement:
    def __init__(self, statement):
        self.statement = statement

    def accept(self, visitor):
        visitor.visitStatement(self)

class AssignStmt:
    def __init__(self, op_left, operation, op_right):
        self.left = op_left
        self.right = op_right
        self.op = operation

    def accept(self, visitor):
        visitor.visitAssignStmt(self)

class IfStmt:

    def __init__(self, cond, body, Else):
        self.cond = cond
        self.then = body
        self.Else = Else

    def accept(self, visitor):
        visitor.visitIfStmt(self)

class ElseStmt:
    def __init__(self, cond, body):
        self.cond = cond
        self.then = body

    def accept(self, visitor):
        visitor.visitElseStmt(self)

class WhileStmt:
    def __init__(self, expression, body):
        self.cond = expression
        self.then = body

    def accept(self, visitor):
        visitor.visitWhileStmt(self)

class Expression:

    def __init__(self, op_left, operation, op_right):
        self.left = op_left
        self.right = op_right
        self.op = operation

    def accept(self, visitor):
        visitor.visitExpression(self)

class Conjunction:
    def __init__(self, primary):
        self.primary = primary

    def accept(self, visitor):
        visitor.visitConjunction(self)

class Equality:
    def __init__(self, left, equop, right):
        self.left = left
        self.equop = equop
        self.right = right

    def accept(self, visitor):
        visitor.visitEquality(self)

class Relation:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def accept(self, visitor):
        visitor.visitRelation(self)

class Addition:
    def __init__(self, term):
        self.term = term

    def accept(self, visitor):
        visitor.visitAddition(self)

class Term:
    def __init__(self, factor):
        self.factor = factor

    def accept(self, visitor):
        visitor.visitTerm(self)

class Factor:
    def __init__(self, unaryop, primary):
        self.unaryop = unaryop
        self.primary = primary

    def accept(self, visitor):
        visitor.visitFactor(self)

class Primary:
    def __init__(self, identifier, expression, literal, parenth):
        self.identifier = identifier
        self.expression = expression
        self.literal = literal
        self.parenth = parenth

    def accept(self, visitor):
        visitor.visitPrimary(self)

class Parenth:
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        visitor.visitParenth(self)

#ast = Body([Statement(AssignStmt(Identifier("X"),"=",Identifier("Y"))),
 #           WhileStmt(Expression(Conjunction(Primary(None,"True",None)),None,None),
  #                    Body(IfStmt(Expression(Identifier("a"),"==",Identifier("b")),
   #                               Body(AssignStmt(Identifier("x"),"=",Identifier("y"))),
    #                              ElseStmt(None,Body(AssignStmt(Identifier("y"),"=",Identifier("x")))))))])


