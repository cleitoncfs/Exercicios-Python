# Definindo a base de dados de livros como uma lista de dicionários
biblioteca = []

# Função para adicionar um novo livro
def adicionar_livro(autor, titulo, categoria, duracao, emprestado=False):
    livro = {
        'autor': autor,
        'titulo': titulo,
        'categoria': categoria,
        'duracao': duracao,
        'emprestado': emprestado
    }
    biblioteca.append(livro)
    print(f"Livro '{titulo}' adicionado com sucesso!")

# Função para marcar um livro como emprestado
def marcar_como_emprestado(titulo):
    for livro in biblioteca:
        if livro['titulo'] == titulo:
            livro['emprestado'] = True
            print(f"Livro '{titulo}' marcado como emprestado.")
            return
    print(f"Livro '{titulo}' não encontrado na biblioteca.")

# Função para mostrar todos os livros de uma determinada categoria
def mostrar_livros_por_categoria(categoria):
    livros_categoria = [livro for livro in biblioteca if livro['categoria'] == categoria]
    if livros_categoria:
        print(f"Livros na categoria '{categoria}':")
        for livro in livros_categoria:
            status = 'Emprestado' if livro['emprestado'] else 'Disponível'
            print(f"- {livro['titulo']} por {livro['autor']} ({status})")
    else:
        print(f"Não há livros na categoria '{categoria}'.")

# Exemplo
adicionar_livro('J.K. Rowling', 'Harry Potter e a Pedra Filosofal', 'Fantasia', '8h 17m')
adicionar_livro('George Orwell', '1984', 'Distopia', '11h 22m')
adicionar_livro('J.R.R. Tolkien', 'O Senhor dos Anéis', 'Fantasia', '22h 38m')

marcar_como_emprestado('1984')

mostrar_livros_por_categoria('Fantasia')
