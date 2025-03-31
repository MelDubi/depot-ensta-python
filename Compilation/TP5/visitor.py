class Visitor:
    def visitAst(self, ast):
        ast.accept(self)

    def visitProgram(self, program):
        for declaration in program.declarations:
            declaration.accept(self)
        for statement in program.statements:
            statement.accept(self)

    def visitCircuit(self, circuit):
        circuit.identifier.accept(self)

    def visitBody(self, body):
        for my_body in body:
            my_body.accept(self)

    def visitInput(self, input):
        input.input.accept(self)

    def visitOutput(self, output):
        output.output.accept(self)

    def visitStatement(self, statement):
        statement.statement.accept(self)

    def visitAssignStmt(self, assignStmt):
        assignStmt.left.accept(self)
        assignStmt.right.accept(self)
        assignStmt.op.accept(self)

    def visitIfStmt(self, ifstmt):
        ifstmt.cond.accept(self)
        ifstmt.then.accept(self)
        ifstmt.Else.accept(self)

    def visitElseStmt(self, elsestmt):
        elsestmt.cond.accept(self)
        elsestmt.then.accept(self)

    def visitWhileStmt(self, whilestmt):
        whilestmt.cond.accept(self)
        whilestmt.then.accept(self)

    def visitExpression(self, expression):
        expression.left.accept(self)
        expression.right.accept(self)
        expression.op.accept(self)

    def visitConjuction(self, conjunction):
        conjunction.primary.accept(self)

    def visitEquality(self, equality):
        equality.left.accept(self)
        equality.equop.accept(self)
        equality.right.accept(self)

    def visitRelation(self, relation):
        relation.left.accept(self)
        relation.equop.accept(self)
        relation.right.accept(self)

    def visitAddition(self, addition):
        addition.term.accept(self)

    def visitTerm(self, term):
        term.factor.accept(self)

    def visitFactor(self, factor):
        factor.unaryop.accept(self)
        factor.primary.accept(self)

    def visitPrimary(self, primary):
        primary.identifier.accept(self)
        primary.expression.accept(self)
        primary.literal.accept(self)
        primary.parenth.accept(self)

    def visitParenth(self, parenth):
        parenth.expression.accept(self)












