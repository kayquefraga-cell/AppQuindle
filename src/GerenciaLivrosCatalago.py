from FilaLivros import filaLivros
import json

def gerenciar_fila_livros():
    livro = filaLivros.get()
    arq = open('catalogo_livros.json', 'r', encoding='utf-8')
    catalogo = json.load(arq)
    arq.close()
    for livro in catalogo:
        try:
            print(f"Livro: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}")
        except KeyError as e:
            print(f"Erro ao acessar dados do livro: {e}")
    print("Livro processado com sucesso.")
    filaLivros.task_done()
