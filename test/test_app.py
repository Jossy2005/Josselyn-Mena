from app import app


def test_home():
    client = app.test_client()
    response = client.get('/')

    assert response.status_code == 200
    assert "¡Hola desde mi aplicación!" in response.get_data(as_text=True)


def test_saludo_personalizado():
    client = app.test_client()
    nombre = "Josselyn"
    response = client.get(f'/saludo/{nombre}')

    assert response.status_code == 200
    assert f"¡Hola, {nombre}!" in response.get_data(as_text=True)
