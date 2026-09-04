from flask import Flask, render_template, url_for, redirect, request, session
import models

app = Flask(__name__)
app.config["SECRET_KEY"] = "psi-atividade1"


@app.get("/")
def index():
    q = request.args.get("q", "")
    livros = models.buscar_livros(q)
    return render_template("index.html", livros=livros)


@app.get("/livro/<int:livro_id>")
def detalhe_livro(livro_id):
    livro = models.buscar_livro(livro_id)

    if livro is None:
        return "Livro não encontrado", 404

    resenhas = models.resenhas_do_livro(livro_id)
    return render_template("livro.html", livro=livro, resenhas=resenhas)


@app.post("/livro/<int:livro_id>/resenhar")
def resenhar(livro_id):
    if "usuario" not in session:
        return redirect(url_for("login"))

    texto = request.form.get("texto", "").strip()
    nota_raw = request.form.get("nota")
    try:
        nota = int(nota_raw)
    except Exception:
        nota = None

    novo_id = models.proximo_id_resenha
    nova_resenha = {
        "id": novo_id,
        "livro_id": livro_id,
        "usuario": session.get("usuario"),
        "texto": texto,
        "nota": nota,
    }
    models.resenhas.append(nova_resenha)
    models.proximo_id_resenha += 1

    return redirect(url_for("detalhe_livro", livro_id=livro_id))


@app.route("/login", methods=["GET", "POST"])
def login():
    erro = None

    if request.method == "POST":
        nome = request.form.get("nome")
        senha = request.form.get("senha")

        usuario = next(
            (u for u in models.usuarios if u["nome"] == nome and u["senha"] == senha),
            None,
        )

        if usuario:
            session["usuario"] = usuario["nome"]
            return redirect(url_for("index"))

        erro = "Nome ou senha inválidos."

    return render_template("login.html", erro=erro)


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    erro = None

    if request.method == "POST":
        nome = request.form.get("nome")
        senha = request.form.get("senha")

        if not nome or not senha:
            erro = "Preencha nome e senha."
        elif any(u["nome"] == nome for u in models.usuarios):
            erro = "Este nome de usuário já existe."
        else:
            novo_usuario = {
                "id": len(models.usuarios) + 1,
                "nome": nome,
                "senha": senha,
            }
            models.usuarios.append(novo_usuario)
            session["usuario"] = nome
            return redirect(url_for("index"))

    return render_template("cadastro.html", erro=erro)


@app.get("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)