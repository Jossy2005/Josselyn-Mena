from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    
    assert response.status_code == 200
    assert b"¡Hola desde mi aplicación!" in response.data

def test_saludo_personalizado():
    client = app.test_client()
    nombre = "Josselyn"
    response = client.get(f'/saludo/{nombre}')

    assert response.status_code == 200
    assert bytes(f"¡Hola, {nombre}!", "utf-8") in response.data
