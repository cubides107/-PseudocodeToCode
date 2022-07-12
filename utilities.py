def clean_line(line):
    return line.strip()


# Definir las variables con el tipo de dato(Construir substring)
def definir(vars, type_vars):
    return '\t' + type_vars.strip() + ' ' + vars + ';\n'


# Obtener index de substring de una cadena
def get_index_substring(string, sub_string):
    return string.index(sub_string)


# Obtener nombre de las varibles
def get_vars(line):
    index = get_index_substring(line, 'Como')
    return line[8:index]


# Obtener typo de variable
def check_type_variables(line):
    index = get_index_substring(line, 'Como')
    index = index + 5
    return line[index:]
