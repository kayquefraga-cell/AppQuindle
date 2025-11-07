from FilaLivros import filaLivros

def gerenciar_fila_livros():
    # Exemplo de uso da fila de livros
    filaLivros.put("Livro A")
    filaLivros.put("Livro B")
    filaLivros.put("Livro C")

    while not filaLivros.empty():
        livro_atual = filaLivros.get()
        print(f"Lendo: {livro_atual}")