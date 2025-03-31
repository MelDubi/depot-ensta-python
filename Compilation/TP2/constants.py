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

    (r"main", "KW_MAIN"),

    (r"=", "ASSIGN"),
    (r'\+', 'ADDITION'),
    (r'\-', 'SUBSTRACTION'),
    (r'\/', 'DIVISION'),
    (r'\*', 'MULTIPLICATION'),
    (r'\^', 'XOR'),
    (r'\!\=', 'DIFFERENCE'),
    (r'\<',  'INFERIOR'),
    (r'\>',  'SUPERIOR'),
    (r'\=\=', 'EQUALITY'),
    (r'\<\=', 'INFERIOR_EQUALITY'),
    (r'\=\>', 'SUPERIOR_EQUALITY'),
    (r'\%',  'MODULO'),
    (r'\&\&',  'AND'),
    (r'\|\|',  'OR'),
    (r'\!',  'NOT'),

    (r'\(', 'OPEN_BRACKET'),
    (r'\)', 'CLOSE_BRACKET'),
    (r'\[', 'OPEN_HOOK'),
    (r'\]', 'CLOSE_HOOK'),
    (r';', 'SEMICOLON'),
    (r'%', 'MODULO'),
    (r'.', 'VIRGULE'),

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

    (r"\w", "IDENTIFIER"),
    (r'.*".*".*', 'STRING'),
    (r"-?\d+", "INTEGER"),
    (r"-?\d+(\.\d*)?", "FLOAT"),

]
