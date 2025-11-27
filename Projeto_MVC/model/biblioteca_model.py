import psycopg2

class Database:
    
    def __init__(self):
        
        self.conn_params = {
            "host": "localhost",
            "dbname": "biblioteca", 
            "user": "postgres", 
            "password": "Admin123",
            "port": "5432"
        }
        self.conn = None
        self.cursor = None
        self._conectar()

    def _conectar(self):
        
        try:
            self.conn = psycopg2.connect(**self.conn_params)
            self.cursor = self.conn.cursor()
        except psycopg2.Error as e:
            print(f"Erro ao conectar ao PostgreSQL: {e}")
            self.conn = None

    def _desconectar(self):
        
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def execute(self, query, params=None, commit=False, fetch=False, fetch_one=False):
        
        if not self.conn:
            return None

        try:
            self.cursor.execute(query, params)
            if commit:
                self.conn.commit()
            
            if fetch:
                return self.cursor.fetchall()
            elif fetch_one:
                return self.cursor.fetchone()
            
        except psycopg2.Error as e:
            print(f"Erro ao executar a query: {e}")
            self.conn.rollback()
            return None
        finally:
            if not (fetch or fetch_one): 
                self._desconectar()

class BibliotecaModel:
    """Contém a lógica de negócio e as operações CRUD."""
    
    def __init__(self):
        self.db = Database()

    
    def cadastrar_autor(self, nome, nacionalidade):
        sql = "INSERT INTO Autor (nome, nacionalidade) VALUES (%s, %s) RETURNING id;"
        
        db = Database()
        resultado = db.execute(sql, (nome, nacionalidade), commit=True, fetch_one=True)
        return resultado[0] if resultado else None

    def listar_autores(self):
        sql = "SELECT id, nome, nacionalidade FROM Autor ORDER BY nome;"
        db = Database()
        return db.execute(sql, fetch=True)

    def atualizar_autor(self, autor_id, nome, nacionalidade):
        sql = "UPDATE Autor SET nome = %s, nacionalidade = %s WHERE id = %s;"
        db = Database()
        db.execute(sql, (nome, nacionalidade, autor_id), commit=True)
        
        return db.cursor.rowcount > 0 

    def excluir_autor(self, autor_id):
        sql = "DELETE FROM Autor WHERE id = %s;"
        db = Database()
        db.execute(sql, (autor_id,), commit=True)
        return db.cursor.rowcount > 0

    
    def cadastrar_livro(self, titulo, ano_publicacao, autor_id):
        sql = "INSERT INTO Livro (titulo, ano_publicacao, autor_id) VALUES (%s, %s, %s) RETURNING id;"
        db = Database()
        resultado = db.execute(sql, (titulo, ano_publicacao, autor_id), commit=True, fetch_one=True)
        return resultado[0] if resultado else None

    def listar_livros(self):
        
        sql = """
        SELECT L.id, L.titulo, L.ano_publicacao, A.nome
        FROM Livro L
        JOIN Autor A ON L.autor_id = A.id
        ORDER BY L.titulo;
        """
        db = Database()
        return db.execute(sql, fetch=True)

    def atualizar_livro(self, livro_id, titulo, ano_publicacao, autor_id):
        sql = "UPDATE Livro SET titulo = %s, ano_publicacao = %s, autor_id = %s WHERE id = %s;"
        db = Database()
        db.execute(sql, (titulo, ano_publicacao, autor_id, livro_id), commit=True)
        return db.cursor.rowcount > 0

    def excluir_livro(self, livro_id):
        sql = "DELETE FROM Livro WHERE id = %s;"
        db = Database()
        db.execute(sql, (livro_id,), commit=True)
        return db.cursor.rowcount > 0

    def autor_existe(self, autor_id):
        
        sql = "SELECT 1 FROM Autor WHERE id = %s;"
        db = Database()
        return db.execute(sql, (autor_id,), fetch_one=True) is not None
            

    