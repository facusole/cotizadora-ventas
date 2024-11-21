import pytest
import os
from proyectoFinal import verify_credentials, save_users, load_users

# Ruta temporal para pruebas
TEST_USERS_FILE = "test_usuarios.json"


@pytest.fixture(autouse=True)
def setup_and_teardown():
    """Fixture para preparar el entorno antes y después de cada prueba."""
    # Asegura que no exista el archivo antes de las pruebas
    if os.path.exists(TEST_USERS_FILE):
        os.remove(TEST_USERS_FILE)

    yield  # Ejecución de las pruebas

    # Limpia después de las pruebas
    if os.path.exists(TEST_USERS_FILE):
        os.remove(TEST_USERS_FILE)

    
def test_verify_credentials():
    """Prueba para verificar credenciales correctamente."""
    mock_users = {"user1": "password1", "user2": "password2"}
    save_users(mock_users, TEST_USERS_FILE)  # Guardamos los usuarios

    # Verifica credenciales
    assert verify_credentials("user1", "password1", TEST_USERS_FILE) is True
    assert verify_credentials("user2", "password2", TEST_USERS_FILE) is True
    assert verify_credentials("user3", "password3", TEST_USERS_FILE) is False  # Usuario no existe
    assert verify_credentials("user1", "wrong_password", TEST_USERS_FILE) is False  # Contraseña incorrecta


def test_save_and_load_users():
    """Prueba para verificar que los usuarios se guarden y carguen correctamente."""
    mock_users = {"user1": "password1", "user2": "password2"}

    # Simula guardar usuarios
    save_users(mock_users, TEST_USERS_FILE)

    # Carga desde el archivo
    loaded_users = load_users(TEST_USERS_FILE)
    assert loaded_users == mock_users
