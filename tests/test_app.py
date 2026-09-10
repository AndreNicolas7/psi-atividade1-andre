from app import app


def test_blueprints_are_registered():
    endpoints = {rule.endpoint for rule in app.url_map.iter_rules()}
    assert "catalog.index" in endpoints
    assert "catalog.ver_livro" in endpoints
    assert "auth.login" in endpoints
    assert "reviews.resenhar" in endpoints
