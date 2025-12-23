class BibliotecaView:
    @staticmethod
    def menu_principal():
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Gerenciar autor")
        print("2 - Gerenciar livro")
        print("3 - Sair")
        try:
            return int(input("\nEscolha uma opção: "))
        except ValueError:
            print('\nEntrada inválida. Digite um número.')
            return -1
        
    @staticmethod
    def submenu_autor():
        print("\n===== Gerenciar Autor =====")
        print("1 - Cadastrar autor")
        print("2 - Listar autores")
        print("3 - Atualizar autor")
        print("4 - Excluir autor")
        print("5 - Voltar ao menu principal")
        try:
            return int(input("\nEscolha uma opção: "))
        except ValueError:
            print('\nEntrada inválida. Digite um número.')
            return -1
        
    @staticmethod
    def submenu_livro():
        print("\n===== Gerenciar Livro =====")
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("3 - Atualizar livro")
        print("4 - Excluir livro")
        print("5 - Voltar ao menu principal")
        try:
            return int(input("\nEscolha uma opção: "))
        except ValueError:
            print('\nEntrada inválida. Digite um número.')
            return -1  
            
    @staticmethod
    def listar_livros(livros):
        if not livros:
            print("\nNenhum livro cadastrado.\n")
        else:
            print("\n=== Lista de livros ===\n")
            for p in livros:
                print(f"ID: {p[0]} | Titulo: {p[1]} | Autor: {p[2]}")
            
    @staticmethod
    def listar_autores(autores):
        if not autores:
            print("\nNenhum autor cadastrado.\n")
        else:
            print("\n=== Lista de autores ===\n")
            for p in autores:
                print(f"ID: {p[0]} | Autor: {p[1]} | Nacionalidade: {p[2]}")

    @staticmethod
    def cadastrar_autor():
        nome = input("Nome do autor: ")
        nacionalidade = input("Nacionalidade: ")
        return nome, nacionalidade
    
    @staticmethod
    def cadastrar_livro():
        titulo = input("Titulo: ")
        id_autor = int(input("ID autor: "))
        try:
            ano_publicacao = int(input("Ano de publicação: "))
            return titulo, id_autor, ano_publicacao
        except Exception as e:
            print("\nNúmero inválido para ano.\n")
            return None, None, None
        
    
    @staticmethod
    def atualizar_autor():
        try:
            id_autor = int(input("ID do autor a atualizar: "))
            nome = input("Novo nome: ")
            nacionalidade = input("Nova nacionalidade: ")
            return id_autor, nome, nacionalidade
        except ValueError:
            print("\nEntrada inválida.\n")
            return None, None, None
        
    @staticmethod
    def atualizar_livro():
        try:
            id_livro = int(input("ID do livro a atualizar: "))
            titulo = input("Novo título: ")
            ano_publicacao = int(input("Novo ano de publicação: "))
            id_autor = int(input("Novo ID autor: "))
            return id_livro, titulo, id_autor, ano_publicacao
        except ValueError:
            print("\nEntrada inválida.\n")
            return None, None, None, None
        
    @staticmethod
    def excluir_autor():
        try:
            id_autor = int(input("ID do autor a excluir: "))
            return id_autor
        except ValueError:
            print("\nEntrada inválida.\n")
            return None
        
    @staticmethod
    def excluir_livro():
        try:
            id_livro = int(input("ID do livro a excluir: "))
            return id_livro
        except ValueError:
            print("\nEntrada inválida.\n")
            return None
    
    @staticmethod
    def mensagem(msg):
        print(msg)