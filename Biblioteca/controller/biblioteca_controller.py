from model.biblioteca_model import BibliotecaModel
from view.biblioteca_view import BibliotecaView

class BibliotecaController:
    def __init__(self):
        self.model = BibliotecaModel()
        self.view = BibliotecaView()

    def executar(self):
        while True:
            opcao = self.view.menu_principal()

            if opcao == 1:
                self.menu_autor()

            elif opcao == 2:
                self.menu_livro()

            elif opcao == 3:
                self.view.mensagem("Saindo...")
                break
            else:
                self.view.mensagem("Opção inválida.")
    
    def menu_autor(self):
        while True:
            opcao = self.view.submenu_autor()

            if opcao == 1:
                self.cadastrar_autor()
            elif opcao == 2:
                self.listar_autores()
            elif opcao == 3:
                self.atualizar_autor()
            elif opcao == 4:
                self.excluir_autor()
            elif opcao == 5:
                break
            else: 
                self.view.mensagem("Opção inválida.")
             
    def cadastrar_autor(self):
        nome, nacionalidade = self.view.cadastrar_autor()
        self.model.inserir_autor(nome, nacionalidade)
        self.view.mensagem("\nAutor cadastrado com sucesso!\n")


    def listar_autores(self):
        autores = self.model.listar_autores()
        if not autores:
            self.view.mensagem("\nNenhum autor cadastrado.\n")
            return None

        self.view.listar_autores(autores)
        return autores

    def atualizar_autor(self):
        autores = self.listar_autores()
        if autores is None:
            return  
        id_autor, nome, nacionalidade = self.view.atualizar_autor()

        if id_autor is None:
            return

        if not self.model.existe_idautor(id_autor):
            self.view.mensagem("\nERRO: Autor não encontrado!\n")
            return

        self.model.atualizar_autor(id_autor, nome, nacionalidade)
        self.view.mensagem("\nAutor atualizado com sucesso!\n")

    def excluir_autor(self):
        autores = self.listar_autores()
        if autores is None:
            return

        id_autor = self.view.excluir_autor()

        if id_autor is None:
            return

        if not self.model.existe_idautor(id_autor):
            self.view.mensagem("\nERRO: Autor não encontrado!\n")
            return

        sucesso = self.model.excluir_autor(id_autor)
        if sucesso:
            self.view.mensagem("\nAutor excluído com sucesso!\n")
        
    def menu_livro(self):
        while True:
            opcao = self.view.submenu_livro()

            if opcao == 1:
                self.cadastrar_livro()
            elif opcao == 2:
                self.listar_livros()
            elif opcao == 3:
                self.atualizar_livro()
            elif opcao == 4:
                self.excluir_livro()
            elif opcao == 5:
                break
            else: 
                self.view.mensagem("Opção inválida.")
            
    def cadastrar_livro(self):
        autores = self.model.listar_autores()

        if not autores:
            self.view.mensagem("\nERRO: Não há autores cadastrados! Cadastre um autor antes de cadastrar livros.\n")
            return

        self.view.listar_autores(autores)

        titulo, id_autor, ano_publicacao = self.view.cadastrar_livro()

        if id_autor is None:
            return

        if not self.model.existe_idautor(id_autor):
            self.view.mensagem("\nERRO: ID de autor não existe!\n")
            return

        self.model.inserir_livro(titulo, id_autor, ano_publicacao)
        self.view.mensagem("\nLivro cadastrado com sucesso!\n")

    def listar_livros(self):
        livros = self.model.listar_livros() 
        if not livros:
            self.view.mensagem("\nNenhum livro cadastrado.\n")
            return
        self.view.listar_livros(livros)
        return livros

    def atualizar_livro(self):
        livros = self.model.listar_livros() 
        if not livros:
            self.view.mensagem("\nNenhum livro cadastrado.\n")
            return
        self.view.listar_livros(livros)

        id_livro, titulo, id_autor, ano_publicacao = self.view.atualizar_livro()

        if id_livro is None:
            return

        if not self.model.existe_idlivro(id_livro):
            self.view.mensagem("\nERRO: Livro não encontrado!\n")
            return
        
        if not self.model.existe_idautor(id_autor):
            self.view.mensagem("\nERRO: Autor não existe!\n")
            return

        self.model.atualizar_livro(id_livro, titulo, id_autor, ano_publicacao)
        self.view.mensagem("\nLivro atualizado com sucesso!\n")


    def excluir_livro(self):
        livros = self.model.listar_livros() 
        if not livros:
            self.view.mensagem("\nNenhum livro cadastrado.\n")
            return
        self.view.listar_livros(livros)
        
        id_livro = self.view.excluir_livro()

        if id_livro is None:
            return

        if not self.model.existe_idlivro(id_livro):
            self.view.mensagem("\nERRO: Livro não encontrado!\n")
            return

        sucesso = self.model.excluir_livro(id_livro)
        if sucesso:
            self.view.mensagem("\nLivro excluído com sucesso!\n")