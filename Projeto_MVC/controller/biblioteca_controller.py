from model.biblioteca_model import BibliotecaModel
from view.biblioteca_view import BibliotecaView

class BibliotecaController:
    
    
    def __init__(self):
        self.model = BibliotecaModel()
        self.view = BibliotecaView()
    
    
    def rodar(self):
        """Inicia o loop principal do programa."""
        while True:
            opcao = self.view.menu_principal()
            
            if opcao == '1':
                self.gerenciar_autor_loop()
            elif opcao == '2':
                self.gerenciar_livro_loop()
            elif opcao == '3':
                self.view.mostrar_saida()
                break
            else:
                self.view.mostrar_erro("Opção inválida.")

    def gerenciar_autor_loop(self):
        
        while True:
            opcao = self.view.menu_autor()
            
            if opcao == '1':
                self.cadastrar_autor()
            elif opcao == '2':
                self.listar_autores()
            elif opcao == '3':
                self.atualizar_autor()
            elif opcao == '4':
                self.excluir_autor()
            elif opcao == '5':
                break 
            else:
                self.view.mostrar_erro("Opção inválida.")

    def gerenciar_livro_loop(self):
        """Loop do submenu de Livro."""
        while True:
            opcao = self.view.menu_livro()
            
            if opcao == '1':
                self.cadastrar_livro()
            elif opcao == '2':
                self.listar_livros()
            elif opcao == '3':
                self.atualizar_livro()
            elif opcao == '4':
                self.excluir_livro()
            elif opcao == '5':
                break 
            else:
                self.view.mostrar_erro("Opção inválida.")
                
    

    def cadastrar_autor(self):
        nome, nacionalidade = self.view.input_autor()
        if nome and nacionalidade:
            autor_id = self.model.cadastrar_autor(nome, nacionalidade)
            if autor_id:
                self.view.mostrar_sucesso(f"Autor '{nome}' cadastrado com sucesso. (ID: {autor_id})")
            else:
                self.view.mostrar_erro("Falha ao cadastrar autor. Verifique a conexão com o BD.")

    def listar_autores(self):
        autores = self.model.listar_autores()
        self.view.mostrar_autores(autores)

    def atualizar_autor(self):
        autor_id = self.view.input_autor_id()
        if autor_id is None: return

        
        if not self.model.autor_existe(autor_id):
            self.view.mostrar_erro(f"Autor com ID {autor_id} não encontrado.")
            return

        nome, nacionalidade = self.view.input_autor(modo="Atualização")
        if nome and nacionalidade:
            if self.model.atualizar_autor(autor_id, nome, nacionalidade):
                self.view.mostrar_sucesso(f"Autor ID {autor_id} atualizado com sucesso.")
            else:
                self.view.mostrar_erro("Falha ao atualizar autor.")

    def excluir_autor(self):
        autor_id = self.view.input_autor_id()
        if autor_id is None: return

        if self.model.excluir_autor(autor_id):
            
            self.view.mostrar_sucesso(f"Autor ID {autor_id} e seus livros associados excluídos com sucesso.")
        else:
            self.view.mostrar_erro(f"Falha ao excluir autor. ID {autor_id} não encontrado ou erro de BD.")

    

    def cadastrar_livro(self):
        titulo, ano, autor_id = self.view.input_livro()
        
        if not self.model.autor_existe(autor_id):
            self.view.mostrar_erro(f"Não é possível cadastrar: Autor com ID {autor_id} não encontrado.")
            return

        livro_id = self.model.cadastrar_livro(titulo, ano, autor_id)
        if livro_id:
            self.view.mostrar_sucesso(f"Livro '{titulo}' cadastrado com sucesso. (ID: {livro_id})")
        else:
            self.view.mostrar_erro("Falha ao cadastrar livro.")

    def listar_livros(self):
        livros = self.model.listar_livros()
        self.view.mostrar_livros(livros)

    def atualizar_livro(self):
        livro_id = self.view.input_livro_id()
        if livro_id is None: return

        titulo, ano, autor_id = self.view.input_livro(modo="Atualização")

        if not self.model.autor_existe(autor_id):
            self.view.mostrar_erro(f"Não é possível atualizar: Autor com ID {autor_id} não encontrado.")
            return

        if self.model.atualizar_livro(livro_id, titulo, ano, autor_id):
            self.view.mostrar_sucesso(f"Livro ID {livro_id} atualizado com sucesso.")
        else:
            self.view.mostrar_erro(f"Falha ao atualizar livro. ID {livro_id} não encontrado.")

    def excluir_livro(self):
        livro_id = self.view.input_livro_id()
        if livro_id is None: return

        if self.model.excluir_livro(livro_id):
            self.view.mostrar_sucesso(f"Livro ID {livro_id} excluído com sucesso.")
        else:
            self.view.mostrar_erro(f"Falha ao excluir livro. ID {livro_id} não encontrado ou erro de BD.")
