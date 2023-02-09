from ting_file_management.file_management import txt_importer
import sys

def process(path_file, instance):
    index = 0
    while index < instance.__len__():
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return

    result = txt_importer(path_file)

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(result),
        "linhas_do_arquivo": result
    }

    print(data)
    instance.enqueue(data)


def remove(instance):
    if not instance.__len__():
        print('Não há elementos')
    else:
        file = instance.dequeue()
        print(f'Arquivo {file["nome_do_arquivo"]} removido com sucesso')


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        print(file)
        return
    except Exception as err:
        print(err, file=sys.stderr)