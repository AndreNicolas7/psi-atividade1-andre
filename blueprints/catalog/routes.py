from flask import render_template, request

import models
from . import catalog_bp


@catalog_bp.route("/")
def index():
    q = request.args.get("q", "")
    return render_template("catalog/index.html", livros=models.buscar_livros(q), q=q)


@catalog_bp.route("/livro/<int:livro_id>")
def ver_livro(livro_id):
    livro = models.buscar_livro(livro_id)
    if livro is None:
        return "Livro não encontrado", 404
    return render_template(
        "catalog/livro.html",
        livro=livro,
        resenhas=models.resenhas_do_livro(livro_id),
    )
