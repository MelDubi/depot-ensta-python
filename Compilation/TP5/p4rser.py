import logging
import ast as ast

logger = logging.getLogger(__name__)


class ParsingException(Exception):
    pass


class Parser:
    def __init__(self, lexems):
        """
        Component in charge of syntaxic analysis.
        """
        self.lexems = lexems

    # ==========================
    #      Helper Functions
    # ==========================

    def accept(self):
        """
        Pops the lexem out of the lexems list.
        """
        self.show_next()
        return self.lexems.pop(0)

    def show_next(self, n=1):
        """
        Returns the next token in the list WITHOUT popping it.
        """
        try:
            return self.lexems[n - 1]
        except IndexError:
            self.error("No more lexems left.")

    def expect(self, kind):
        """
        Pops the next token from the lexems list and tests its type through the tag.
        """
        next_lexem = self.show_next()
        if next_lexem.kind != kind:
            raise ParsingException(
                f"ERROR at {str(self.show_next().position)}: Expected {kind}, got {next_lexem.tag} instead"
            )
        return self.accept()

    def remove_comments(self):
        """
        Removes the comments from the token list by testing their tags.
        """
        self.lexems = [lexem for lexem in self.lexems if lexem.tag != "COMMENT"]

    # ==========================
    #     Parsing Functions
    # ==========================

    def parse(self):
        """
        Main function: launches the parsing operation given a lexem list.
        """
        try:
            self.remove_comments()
            self.parse_program()
        except ParsingException as err:
            logger.exception(err)
            raise

    def parse_program(self):
        """
        Parses a program which is a succession of assignments.
        """
        self.expect("CIRCUIT")
        self.expect("IDENTIFIER")
        program = ast.Program()

        while self.show_next().tag != "END":
            if self.show_next().tag in ["INPUT", "OUTPUT"]:
                program.circuit.append(self.parse_circuit())
            else:
                program.statements.append(self.parse_statement())

    def parse_circuit(self):
        self.accept()
        identifier = None

        if self.show_next().tag == "COMMA":
            self.accept()
            identifier = self.expect("IDENTIFIER")
        elif self.show_next().tag in ["INPUT", "OUTPUT"]:
            identifier = self.expect("IDENTIFIER")
        else
            self.parse_identifier

        return ast.Circuit(identifier)

    def parse_identifier(self):
        statement = None
        if self.show_next().tag == "IF":
            statement = self.parse_if_statement()
        elif self.show_next().tag == "WHILE":
            statement = self.parse_while_statement()
        else:
            statement = self.parse_assignment()
        return ast.Statement(statement)

    def parse_statement(self):
        statement = None
        if self.show_next().tag == "IF":
            statement = self.parse_if_statement()
        elif self.show_next().tag == "WHILE":
            statement = self.parse_while_statement()
        else:
            statement = self.parse_assignment()
        return ast.Statement(statement)

    def parse_assignment(self):
        left = self.expect("IDENTIFIER")

        if self.show_next().tag == "OPEN HOOK":
            self.accept()
            self.parse_expression()
            self.expect("CLOSE HOOK")

        op = self.expect("ASSIGN")
        right = self.parse_expression()
        self.expect("SEMICOLON")

        return ast.AssignStmt(left, op, right)

    def parse_if_statement(self):

        global else_statement
        self.expect("IF")
        self.expect("OPEN BRACKETS")
        expression = self.parse_expression()
        self.expect("CLOSE BRACKETS")
        self.expect("OPEN_CURL_BRACKET")

        body = []
        while self.show_next().tag != "CLOSE_CURL_BRACKET":
            body.append(self.parse_statement())

        self.expect("CLOSE_CURL_BRACKET")

        if self.show_next().tag == "ELSE":
            else_statement = self.parse_else_statement()

        return ast.IfStmt(expression, body, else_statement)

    def parse_else_statement(self):
        self.expect("ELSE")
        self.expect("OPEN_CURL_BRACKET")

        body = []
        while self.show_next().tag != "CLOSE_CURL_BRACKET":
            body.append(self.parse_statement())

        self.expect("CLOSE_CURL_BRACKET")

        return ast.ElseStmt(body)

    def parse_while_statement(self):
        self.expect("WHILE")
        self.expect("OPEN_BRACKET")
        expression = self.parse_expression()
        self.expect("CLOSE_BRACKET")
        self.expect("OPEN_CURL_BRACKET")

        body = []
        while self.show_next().tag != "CLOSE_CURL_BRACKET":
            body.append(self.parse_statement())

        self.expect("CLOSE_CURL_BRACKET")

        return ast.WhileStmt(expression, body)

    def parse_expression(self):
        conjunction = []
        conjunction.append(self.parse_conjunction())
        if self.show_next().tag == "OR":
            conjunction.append(self.accept())
            conjunction.append(self.parse_conjunction())

        return ast.Expression(conjunction)

    def parse_conjunction(self):
        equality = []
        equality.append(self.parse_equality())

        if self.show_next().tag == "AND":
            equality.append(self.accept())
            equality.append(self.parse_equality())

        return ast.Conjunction(equality)

    def parse_equality(self):
        left = self.parse_relation()
        equop = None
        right = None

        if self.show_next().tag in ["EQUALITY", "DIFFERENCE"]:
            equop = self.accept()
            right = self.parse_relation()

        return ast.Equality(left, equop, right)

    def parse_relation(self):
        left = self.parse_addition()
        relop = None
        right = None

        if self.show_next().tag in ["INFERIOR", "INFERIOR_EQUALITY", "SUPERIOR", "SUPERIOR_EQUALITY"]:
            relop = self.accept()
            right = self.parse_addition()

        return ast.Relation(left, relop, right)

    def parse_addition(self):
        term = []
        term.append(self.parse_term())

        while self.show_next().tag in ["ADDITION", "SUBSTRACTION"]:
            term.append(self.accept())
            term.append(self.parse_term())

        return ast.Addition(term)

    def parse_term(self):
        factor = []
        factor.append(self.parse_factor())

        while self.show_next().tag in ["MULTIPLICATION", "DIVISION", "MODULO"]:
            factor.append(self.accept())
            factor.append(self.parse_factor())

        return ast.Term(factor)

    def parse_factor(self):
        unaryop = None
        if self.show_next().tag in ["SUBSTRACTION", "NOT"]:
            unaryop = self.accept()

        primary = self.parse_primary()

        return ast.Factor(unaryop, primary)

    def parse_primary(self):
        identifier = None
        expression = None
        literal = None
        parenth = None

        if self.show_next().tag == "IDENTIFIER":
            identifier = self.accept()
            if self.show_next().tag == "OPEN_HOOK":
                self.accept()
                expression = self.parse_expression()
                self.expect("CLOSE_HOOK")
        elif self.show_next().tag in ["STRING", "INTEGER", "FLOAT", "TRUE", "FALSE"]:
            literal = self.accept()
        elif self.show_next().tag == "OPEN_BRACKET":
            parenth = self.parse_parenth()

        return ast.Primary(identifier, expression, literal, parenth)

    def parse_parenth(self):
        self.expect("OPEN_BRACKET")
        expression = self.parse_expression()
        self.expect("CLOSE_BRACKET")

        return ast.Parenth(expression)

    def error(self, stderr):
        print(stderr)