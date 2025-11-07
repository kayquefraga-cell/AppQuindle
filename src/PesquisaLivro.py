from FilaLivros import filaLivros

def pesquisar_livro(titulo):
    # Exemplo de pesquisa na fila de livros
    encontrados = []
    tamanho_fila = filaLivros.qsize()
    
    for _ in range(tamanho_fila):
        livro_atual = filaLivros.get()
        if titulo.lower() in livro_atual.lower():
            encontrados.append(livro_atual)
        filaLivros.put(livro_atual)  # Reinsere o livro na fila
    
    return encontrados if encontrados else "Nenhum livro encontrado."