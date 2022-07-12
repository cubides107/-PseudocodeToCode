import tokens
import utilities
import file

if __name__ == '__main__':
    code = '#include<iostream>\n' + 'using namespace std;\n\n'
    file_var = file.open_file()
    for line in file_var:
        word = line.split()[0]
        line = utilities.clean_line(line)
        if word == 'Definir':
            var = utilities.get_vars(line)
            var = var.replace(' ', '')
            type_vars = utilities.check_type_variables(line)
            type_vars = tokens.type_dates[type_vars.strip()]
            code += utilities.definir(var, type_vars)
        elif word == 'Algoritmo':
            code += tokens.func['Algoritmo']
        elif word == 'Leer':
            code += '\tcin >> ' + 'a' + ';\n'
        elif word == 'FinAlgoritmo':
            code += '\treturn 0;\n'
            code += tokens.func['FinAlgoritmo']
    print(code)
    file.write_file(code)

# print(get_var(file[1].strip()))
# print(check_type_variables(file[1].lstrip()))
# print(get_read_var(file[2].lstrip()))
