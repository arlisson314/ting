from ting_file_management.file_management import txt_importer


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
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
