def test_register_user(client):
    response = client.post("/api/auth/register", json={
        "email": "test@example.com", "password": "secret123"
    })
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"