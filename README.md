
1. MVC: o Model está em models.py, com listas e funções como buscar_livro(). O Controller está em app.py, nas rotas, por exemplo livros = models.buscar_livros(). A View está nos HTML de templates. Se o acesso aos dados ficasse direto nas rotas, o código ficaria mais misturado, difícil de manter e testar.

2. Usamos url_for, como em url_for('detalhe_livro', livro_id=livro['id']), porque o Flask monta a URL correta a partir do nome da rota. Assim, se o caminho mudar, não precisamos procurar e alterar vários links fixos.

3. A session representa o usuário logado. Isso aparece em session["usuario"] = usuario["nome"] e session.clear() no logout. A rota de resenhar deveria verificar a sessão antes de gravar para impedir que alguém não autenticado publique uma resenha. Porém, essa rota de resenhar não existe no código atual; só há a exibição das resenhas.

e esse foi o máximo que deu pra fazer romerito, eu achei IMPRESSIONANTE até, foi desumano um negocio desse, n tem tempo pra nada
