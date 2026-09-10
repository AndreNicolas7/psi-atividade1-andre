from flask import redirect, render_template, request, session, url_for

import models
from . import auth_bp


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        for usuario in models.usuarios:
            if usuario["nome"] == request.form["nome"] and usuario["senha"] == request.form["senha"]:
                session["usuario"] = usuario["nome"]
                return redirect(url_for("catalog.index"))
        return render_template("auth/login.html", erro="Credenciais inválidas")
    return render_template("auth/login.html")


@auth_bp.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("catalog.index"))
