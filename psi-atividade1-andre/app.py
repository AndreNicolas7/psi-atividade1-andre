from flask import Flask

from blueprints.auth import auth_bp
from blueprints.catalog import catalog_bp
from blueprints.reviews import reviews_bp

app = Flask(__name__)
app.secret_key = "chave-secreta"

app.register_blueprint(auth_bp)
app.register_blueprint(catalog_bp)
app.register_blueprint(reviews_bp)

if __name__ == "__main__":
    app.run(debug=True)
