LEXEM_REGEXES = [
    # Whitespace
    (r'[ \n\t]+', None),

    # Comments and whitespaces
    (r"\/\/.*", "COMMENT"),
    (r"[ \t\n]+", None),

    # Special characters
    (r"\(", "OPEN_PARENTHESE"),
    (r"\)", "CLOSE_PARENTHESE"),
    (r"\{", "OPEN_CURL_BRACKET"),
    (r"\}", "CLOSE_CURL_BRACKET"),

    (r'\(', 'OPEN_BRACKET'),
    (r'\)', 'CLOSE_BRACKET'),
    (r'\[', 'OPEN_HOOK'),
    (r'\]', 'CLOSE_HOOK'),
    (r';', 'SEMICOLON'),
    (r'%', 'MODULO'),
    (r'.', 'VIRGULE'),
    (r',', 'COMMA'),

    # Type
    (r'int',   'TYPE_INT'),
    (r'bool',  'TYPE_BOOLEAN'),
    (r'float', 'TYPE_FLOAT'),
    (r'char',  'TYPE_CHAR'),

    # Keywords
    (r'if',    'IF'),
    (r'else',  'ELSE'),
    (r'while', 'WHILE'),
    (r'true', 'TRUE'),
    (r'false', 'FALSE'),

    (r'.*".*".*', 'STRING'),
    (r"-?\d+", "INTEGER"),
    (r"-?\d+(\.\d*)?", "FLOAT"),

    # NEW
    (r"circuit", "CIRCUIT"),
    (r"\w", "IDENTIFIER"),
    (r"end", "END"),
    (r"input", "INPUT"),
    (r"output", "OUTPUT"),
    (r"=", "ASSIGN"),
    (r'add', 'ADDITION'),
    (r'sub', 'SUBSTRACTION'),
    (r'div', 'DIVISION'),
    (r'mul', 'MULTIPLICATION'),
    (r'xor', 'XOR'),
    (r'diff', 'DIFFERENCE'),
    (r'inf',  'INFERIOR'),
    (r'sup',  'SUPERIOR'),
    (r'equal', 'EQUALITY'),
    (r'equal inf', 'INFERIOR_EQUALITY'),
    (r'sup inf', 'SUPERIOR_EQUALITY'),
    (r'modulo',  'MODULO'),
    (r'and',  'AND'),
    (r'or',  'OR'),
    (r'not',  'NOT'),

]
