from FilaLivros import filaLivros
import json

def gerenciar_fila_livros():
    livro = filaLivros.get()
    arq = open('catalogo_livros.json', 'r', encoding='utf-8')
    catalogo = json.load(arq)
    arq.close()
    if livro in catalogo:
        print(f'Livro "{livro}" encontrado no catálogo.')
    else:
        print(f'Livro "{livro}" não encontrado no catálogo.')
    filaLivros.task_done()
