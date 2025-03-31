from visitor import Visitor


def get_indentation(indentation_level):
    return "|   " * indentation_level


class PrettyPrint(Visitor):
    def __init__(self):
        self.output = ""

    def visit(self, node, indentation_level):
        node.accept(self, indentation_level)

    def visitProgram(self, node, indentation_level):
        self.output += get_indentation(indentation_level) + "Programme\n"
        self.visit(node.declarations, indentation_level + 1)
        self.output += get_indentation(indentation_level + 1) + "Statements\n"
        self.visit(node.statements, indentation_level + 2)

    def visitDeclaration(self, node, indentation_level):
        self.output += get_indentation(indentation_level) + "Declaration\n"
        self.visit(node.type_, indentation_level + 1)
        self.visit(node.identifier, indentation_level + 1)
        if node.size:
            self.output += get_indentation(indentation_level + 1) + f"Size({node.size})\n"

    def visitStatement(self, node, indentation_level):
        pass

    def visit_Assignment(self, node, indentation_level):
        self.output += get_indentation(indentation_level) + "Assignment\n"
        self.visit(node.identifier, indentation_level + 1)
        self.visit(node.expression, indentation_level + 2)

    def visit_IfStatement(self, node, indentation_level):
        self.output += get_indentation(indentation_level) + "IfStatement\n"
        self.output += get_indentation(indentation_level + 1) + "Condition\n"
        self.visit(node.condition, indentation_level + 2)
        self.output += get_indentation(indentation_level + 1) + "Body\n"
        self.visit(node.body, indentation_level + 2)
        if node.else_:
            self.output += get_indentation(indentation_level + 1) + "Else\n"
            self.visit(node.else_, indentation_level + 2)

    def visit_Else(self, node, indentation_level):
        self.output += get_indentation(indentation_level) + "Else\n"
        self.visit(node.body, indentation_level + 1)

    def visit_WhileLoop(self, node, indentation_level):
        self.output += get_indentation(indentation_level) + "WhileLoop\n"
        self.output += get_indentation(indentation_level + 1) + "Condition\n"
        self.visit(node.condition, indentation_level + 2)
        self.output += get_indentation(indentation_level + 1) + "Body\n"
        self.visit(node.body, indentation_level + 2)


