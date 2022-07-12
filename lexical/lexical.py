import ply.lex as lex

# List of token names.
reservadas = (
    'INCLUDE',
)

tokens = reservadas + (
    'ENTERO',
    'FLOAT',

    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION'
)

t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'


def t_INCLUDE(t):
    r'include'
    return t


def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_FLOAT(t):
    r'\\d+\\.\\d+'
    t.value = float(t.value)
    return t

def t_COMENTARIO(t):
    r'\.'
    pass

# Sin valor de retorno. Ficha descartada


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

    # Error handling rule


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

    # Build the lexer


lexer = lex.lex()

# Test it out
data = '34.53'


# Tokenize
def prueba():
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)


if __name__ == '__main__':
    prueba()
