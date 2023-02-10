def exists_word(word, instance):

    result = []
    for file in instance.data:
        lines = []
        for index, line in enumerate(file['linhas_do_arquivo']):
            if word.lower() in line.lower():
                lines.append({'linha': index + 1})
        if lines:
            result.append({
                'palavra': word,
                'arquivo': file['nome_do_arquivo'],
                'ocorrencias': lines
            })
    return result


def search_by_word(word, instance):

    result = []
    for file in instance.data:
        lines = []
        for index, line in enumerate(file['linhas_do_arquivo']):
            if word.lower() in line.lower():
                lines.append({'linha': index + 1, 'conteudo': line})
        if lines:
            result.append({
                'palavra': word,
                'arquivo': file['nome_do_arquivo'],
                'ocorrencias': lines
            })
    return result
