import sys

def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        print('Formato inválido', file=sys.stderr)
        return

    try:
        with open(path_file, 'r') as file:
            data = file.read()
            return data.splitlines()
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return