# Leer archivo
def open_file():
    with open("code.txt") as archivo:
        return archivo.readlines()


def write_file(string):
    with open("Output.txt", "w") as text_file:
        text_file.write(string)
