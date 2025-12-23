import psycopg2

class BibliotecaModel:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                host="localhost",
                database="biblioteca",
                user="postgres",
                password="admin"
            )
            self.cursor = self.conn.cursor()
        except Exception as e:
            print("Erro ao conectar ao banco:", e)
            
    def listar_livros(self):
        try:
            self.cursor.execute("SELECT id_livro, titulo, nome FROM livro INNER JOIN autor ON livro.id_autor = autor.id_autor ORDER BY id_livro;")
            return self.cursor.fetchall()
        except Exception as e:
            print("Erro ao listar livros:", e)
            return []
        
    def listar_autores(self):
        try:
            self.cursor.execute("SELECT id_autor, nome, nacionalidade FROM autor ORDER BY id_autor;")
            return self.cursor.fetchall()
        except Exception as e:
            print("Erro ao listar autores:", e)
            return []
        
    def inserir_livro(self, titulo, id_autor, ano_publicacao):
        try:
            self.cursor.execute("INSERT INTO livro (titulo, id_autor, ano_publicacao) VALUES (%s, %s, %s);", (titulo, id_autor, ano_publicacao))
            self.conn.commit()
        except Exception as e:
            print("Erro ao inserir livro:", e)
            self.conn.rollback()
            
    def inserir_autor(self, nome, nacionalidade):
        try:
            self.cursor.execute("INSERT INTO autor (nome, nacionalidade) VALUES (%s, %s);", (nome, nacionalidade))
            self.conn.commit()
        except Exception as e:
            print("Erro ao inserir autor:", e)
            self.conn.rollback()
          
    def existe_idlivro (self, id_livro):
        try:
            self.cursor.execute("select 1 from livro where id_livro=%s;", (id_livro,))
            return self.cursor.fetchone() is not None
        except Exception as e:
            print(f"Erro ao verificar a existência do livro: {e}\n")
            return False
        
    def existe_idautor (self, id_autor):
        try:
            self.cursor.execute("select 1 from autor where id_autor=%s;", (id_autor,))
            return self.cursor.fetchone() is not None
        except Exception as e:
            print(f"Erro ao verificar a existência do autor: {e}\n")
            return False
            
    def atualizar_livro(self, id_livro, titulo, id_autor, ano_publicacao):
        try:
            if not self.existe_idlivro(id_livro):
                print("\nNenhum livro encontrado com esse ID\n")
                return False

            self.cursor.execute("""
                UPDATE livro
                SET titulo = %s,
                    id_autor = %s,
                    ano_publicacao = %s
                WHERE id_livro = %s;
                """, (titulo, id_autor, ano_publicacao, id_livro))
            self.conn.commit()
            return True
        except Exception as e:
            print(f'\nErro ao atualizar livro: {e}\n')
            self.conn.rollback()
            return False

        
    def atualizar_autor(self, id_autor, nome, nacionalidade):
        try:
            if not self.existe_idautor(id_autor):
                print("\nNenhum  autor encontrado com esse ID\n")
                return False
        
            self.cursor.execute("UPDATE autor SET nome = %s, nacionalidade = %s WHERE id_autor = %s;", (nome, nacionalidade, id_autor))
            self.conn.commit()
            return True
        except Exception as e:
            print(f'\nErro ao atualizar autor: {e}\n')
            self.conn.rollback()
            return False
        
    def excluir_livro(self, id_livro):
        try:
            if not self.existe_idlivro(id_livro):
                print("\nNenhum  livro encontrado com esse ID\n")
                return False
        
            self.cursor.execute("delete from livro WHERE id_livro = %s;", (id_livro,))
            self.conn.commit()
            return True
        except Exception as e:
            print(f'\nErro ao excluir livro: {e}\n')
            self.conn.rollback()
            return False
        
    def excluir_autor(self, id_autor):
        try:
            if not self.existe_idautor(id_autor):
                print("\nNenhum  autor encontrado com esse ID\n")
                return False
            self.cursor.execute("SELECT 1 FROM livro WHERE id_autor = %s", (id_autor,))
            if self.cursor.fetchone():
                print("\nAutor possui livros cadastrados. Não é possível excluir.\n")
                return False
        
            self.cursor.execute("delete from autor WHERE id_autor = %s;", (id_autor,))
            self.conn.commit()
            return True
        except Exception as e:
            print(f'\nErro ao excluir autor: {e}\n')
            self.conn.rollback()
            return False
        
        #sempre colocar no model um afunção "destrutor" 
    def __del__(self):
        if hasattr(self, "cursor") and hasattr(self, "conn"):
            self.cursor.close()
            self.conn.close()