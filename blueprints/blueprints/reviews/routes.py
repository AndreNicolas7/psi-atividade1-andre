from flask import redirect, request, session, url_for

import models
from . import reviews_bp


@reviews_bp.route("/livro/<int:livro_id>/resenhar", methods=["POST"])
def resenhar(livro_id):
    if "usuario" not in session:
        return redirect(url_for("auth.login"))
    if models.buscar_livro(livro_id):
        models.resenhas.append({
            "id": models.proximo_id_resenha,
            "livro_id": livro_id,
            "usuario": session["usuario"],
            "texto": request.form["texto"],
            "nota": int(request.form["nota"]),
        })
        models.proximo_id_resenha += 1
    return redirect(url_for("catalog.ver_livro", livro_id=livro_id))
