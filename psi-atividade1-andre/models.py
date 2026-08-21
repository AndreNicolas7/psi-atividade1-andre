# models.py — Camada Model da aplicação
# ============================================================
# ARQUIVO FORNECIDO PELO PROFESSOR — não altere nada aqui.
# Sua tarefa é USAR estes dados e funções a partir do app.py.
#
# Responsabilidade desta camada (Model):
#   - Guardar os dados do sistema (listas de dicionários)
#   - Oferecer funções de busca para o Controller (app.py) usar

usuarios = [
    {"id": 1, "nome": "admin", "senha": "1234"},
    {"id": 2, "nome": "leitor", "senha": "abcd"},
]

livros = [
    {"id": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899, "genero": "Romance"},
    {"id": 2, "titulo": "O Cortiço", "autor": "Aluísio Azevedo", "ano": 1890, "genero": "Naturalismo"},
    {"id": 3, "titulo": "Capitães da Areia", "autor": "Jorge Amado", "ano": 1937, "genero": "Romance"},
    {"id": 4, "titulo": "A Hora da Estrela", "autor": "Clarice Lispector", "ano": 1977, "genero": "Romance"},
]

resenhas = [
    {"id": 1, "livro_id": 1, "usuario": "admin", "texto": "Clássico obrigatório sobre ciúme e narrador não confiável.", "nota": 5},
    {"id": 2, "livro_id": 1, "usuario": "leitor", "texto": "Releitura vale a pena: cada capítulo engana o leitor.", "nota": 4},
    {"id": 3, "livro_id": 3, "usuario": "leitor", "texto": "Retrata com força a Bahia dos anos 1930.", "nota": 4},
]

proximo_id_resenha = 4


def buscar_livro(livro_id):
    """Devolve o livro com o id informado, ou None se não existir."""
    for livro in livros:
        if livro["id"] == livro_id:
            return livro
    return None


def resenhas_do_livro(livro_id):
    """Devolve apenas as resenhas vinculadas ao livro informado."""
    return [r for r in resenhas if r["livro_id"] == livro_id]


def buscar_livros(q=""):
    """Devolve todos os livros; se q for informado, filtra pelo título."""
    if not q:
        return livros
    return [l for l in livros if q.lower() in l["titulo"].lower()]