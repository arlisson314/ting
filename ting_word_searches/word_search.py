def exists_word(word, instance):

    result = []
    for file in instance.data:
        lines = []
        for index, line in enumerate(file['linhas_do_arquivo'], início=0):
            if word.lower() in line.lower():
                lines.append(index + 1)
        if lines:
            result.append({
                'palavra': word,
                'arquivo': file['nome_do_arquivo'],
                'ocorrencias': [{'linha': line_num} for line_num in lines]
            })
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
