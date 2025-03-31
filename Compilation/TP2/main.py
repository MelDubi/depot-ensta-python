from optparse import OptionParser

from lexer import Lexer
from p4rser import Parser

import ast


def main():
    parser = OptionParser()

    parser.add_option("-i",
                      "--input",
                      action="store",
                      type="string",
                      dest="input_file",
                      metavar="INPUT_PATH")

    options, args = parser.parse_args()

    if (not options.input_file):
        parser.print_help()
        exit()

    lexer = Lexer()
    fd = open(options.input_file)
    lines = fd.readlines()
    lexems = lexer.lex(lines)

    print(lexems)

    parser = Parser(lexems)
    ast = parser.parse()


if __name__ == "__main__":
    main()

