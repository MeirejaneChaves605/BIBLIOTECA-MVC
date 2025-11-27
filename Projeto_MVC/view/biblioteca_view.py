import os

class BibliotecaView:
    

    @staticmethod
    def limpar_tela():
        
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def _aguardar_retorno():
        
        input("\nPressione [ENTER] para continuar...")
 
    @staticmethod
    def menu_principal():
        BibliotecaView.limpar_tela()
        print(" Menu Principal")
        print("-------------------")
        print("1. Gerenciar autor")
        print("2. Gerenciar livro")
        print("3. Sair")
        print("-------------------")
        return input("Escolha uma opção: ")

    @staticmethod
    def menu_autor():
        BibliotecaView.limpar_tela()
        print(" Gerenciar Autor")
        print("-----------------")
        print("1. Cadastrar autor")
        print("2. Listar autores")
        print("3. Atualizar autor")
        print("4. Excluir autor")
        print("5. Voltar ao menu principal")
        print("-----------------")
        return input("Escolha uma opção: ")

    @staticmethod
    def menu_livro():
        BibliotecaView.limpar_tela()
        print(" Gerenciar Livro")
        print("-----------------")
        print("1. Cadastrar livro")
        print("2. Listar livros (com autor)")
        print("3. Atualizar livro")
        print("4. Excluir livro")
        print("5. Voltar ao menu principal")
        print("-----------------")
        return input("Escolha uma opção: ")

    @staticmethod
    def input_autor(modo="Cadastro"):
        
        print(f"\n--- {modo} de Autor ---")
        nome = input("Nome do Autor: ")
        nacionalidade = input("Nacionalidade: ")
        return nome, nacionalidade
    
    @staticmethod
    def input_autor_id():
        
        try:
            autor_id = int(input("Informe o ID do Autor: "))
            return autor_id
        except ValueError:
            BibliotecaView.mostrar_erro("ID inválido. Deve ser um número inteiro.")
            return None

    @staticmethod
    def input_livro(modo="Cadastro"):
        """Captura os dados de um livro."""
        print(f"\n--- {modo} de Livro ---")
        titulo = input("Título do Livro: ")
        
        while True:
            try:
                ano = int(input("Ano de Publicação: "))
                if ano <= 0: raise ValueError
                break
            except ValueError:
                BibliotecaView.mostrar_erro("Ano inválido. Deve ser um número inteiro positivo.")
        
        while True:
            try:
                autor_id = int(input("ID do Autor (necessário): "))
                if autor_id <= 0: raise ValueError
                return titulo, ano, autor_id
            except ValueError:
                BibliotecaView.mostrar_erro("ID do Autor inválido. Deve ser um número inteiro positivo.")

    @staticmethod
    def input_livro_id():
        """Captura o ID de um livro."""
        try:
            livro_id = int(input("Informe o ID do Livro: "))
            return livro_id
        except ValueError:
            BibliotecaView.mostrar_erro("ID inválido. Deve ser um número inteiro.")
            return None
        
    @staticmethod
    def mostrar_autores(autores):
        """Exibe a lista de autores."""
        if not autores:
            print("\n❌ Nenhuma autor cadastrado.")
            BibliotecaView._aguardar_retorno()
            return

        print("\n--- Lista de Autores ---")
        print(f"{'ID':<4} | {'Nome':<30} | {'Nacionalidade':<20}")
        print("-" * 59)
        for id, nome, nacionalidade in autores:
            print(f"{id:<4} | {nome:<30} | {nacionalidade:<20}")
        
        BibliotecaView._aguardar_retorno()

    @staticmethod
    def mostrar_livros(livros):
        
        if not livros:
            print("\n Nenhum livro cadastrado.")
            BibliotecaView._aguardar_retorno()
            return

        print("\n--- Lista de Livros ---")
        print(f"{'ID':<4} | {'Título':<40} | {'Ano':<6} | {'Autor'}")
        print("-" * 75)
        for id, titulo, ano, autor_nome in livros:
            print(f"{id:<4} | {titulo:<40} | {ano:<6} | {autor_nome}")
        
        BibliotecaView._aguardar_retorno()

    @staticmethod
    def mostrar_sucesso(mensagem):
        print(f"\n SUCESSO: {mensagem}")
        
    @staticmethod
    def mostrar_erro(mensagem):
        print(f"\n ERRO: {mensagem}")

    @staticmethod
    def mostrar_mensagem(mensagem):
        print(f"\n {mensagem}")

    @staticmethod
    def mostrar_saida():
        print("\n Programa encerrado. Obrigado!")
