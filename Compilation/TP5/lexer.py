import re

import logging

from TP5.constants import LEXEM_REGEXES

logger = logging.getLogger(__name__)

class LexerException(Exception):
    pass

class Lexem:
    def __init__(self, tag, value, position):
        self.tag = tag
        self.value = value
        self.position = position

    def __repr__(self):
        return f"{self.tag}({self.value})"

class Lexer:
    def __init__(self):
        self.lexems = []
        self.current_line_number = 0
        self.current_position = 0

    def lex_file(self, file):
        with open(file, "r") as input_file:
            contents = input_file.readlines()
        return self.lex(contents)

    def lex(self, input):
        for line_nb, line in enumerate(input):
            self.current_position = 0
            self.current_line_number = (
                line_nb + 1
            )  # Python starts at 0, we need to start at 1
            line = line.strip()
            try:
                self.match_line(line)
            except LexerException as err:
                logger.exception(err)
                raise
        return self.lexems

    def match_line(self, line):

        while self.current_position < len(line):
            # Test all regexes in order
            match = False
            for lexem_regex in LEXEM_REGEXES:
                match = self.match_lexem(line, lexem_regex)
                # If a match occurs, break from the loop
                if match:
                    break
            # If all regexes were tested and none matched,
            # raise an error!
            if not match:
                raise LexerException(
                    f"ERROR (lexer) at: ({self.current_line_number},{self.current_position}):\n"
                    + line.strip() + "\n"
                    + " " * len(line[: self.current_position])
                    + "^" * len(line[self.current_position - 1 :])
                    + f"\nLexems: {self.lexems}"
                )

    def match_lexem(self, line, lexem_regex):
        pattern, tag = lexem_regex
        # Compile and match the regex
        regex = re.compile(pattern)
        match = regex.match(line, self.current_position)
        # If a match occured, the result is not None
        if match is not None:
            data = match.group(0)
            # If the match was with a whitespace, its tag is None
            # and we do not need to keep it
            if tag is not None:
                self.append_lexem(tag, data)
            self.current_position = match.end(0)
            return True
        return False

    def append_lexem(self, tag, data):
        lexem = Lexem(tag, data, [self.current_line_number, self.current_position])
        self.lexems.append(lexem)
