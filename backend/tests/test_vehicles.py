import pytest


def test_create_vehicle(client):
    """Test creating a new vehicle"""
    response = client.post("/api/vehicles", json={
        "make": "Toyota",
        "model": "Camry",
        "category": "Sedan",
        "price": 25000.0,
        "quantity": 5
    })
    assert response.status_code == 200
    data = response.json()
    assert data["make"] == "Toyota"
    assert data["model"] == "Camry"
    assert data["category"] == "Sedan"
    assert data["price"] == 25000.0
    assert data["quantity"] == 5


def test_get_all_vehicles(client):
    """Test retrieving all vehicles"""
    # Create a vehicle first
    client.post("/api/vehicles", json={
        "make": "Honda",
        "model": "Civic",
        "category": "Sedan",
        "price": 22000.0,
        "quantity": 3
    })
    
    response = client.get("/api/vehicles")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_vehicle_by_id(client):
    """Test retrieving a specific vehicle by ID"""
    # Create a vehicle first
    create_response = client.post("/api/vehicles", json={
        "make": "Ford",
        "model": "Mustang",
        "category": "Sports",
        "price": 35000.0,
        "quantity": 2
    })
    vehicle_id = create_response.json()["id"]
    
    response = client.get(f"/api/vehicles/{vehicle_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == vehicle_id
    assert data["make"] == "Ford"


def test_update_vehicle(client):
    """Test updating a vehicle"""
    # Create a vehicle first
    create_response = client.post("/api/vehicles", json={
        "make": "BMW",
        "model": "X5",
        "category": "SUV",
        "price": 55000.0,
        "quantity": 1
    })
    vehicle_id = create_response.json()["id"]
    
    # Update the vehicle
    response = client.put(f"/api/vehicles/{vehicle_id}", json={
        "make": "BMW",
        "model": "X5",
        "category": "SUV",
        "price": 54000.0,
        "quantity": 2
    })
    assert response.status_code == 200
    data = response.json()
    assert data["price"] == 54000.0
    assert data["quantity"] == 2


def test_delete_vehicle(client):
    """Test deleting a vehicle"""
    # Create a vehicle first
    create_response = client.post("/api/vehicles", json={
        "make": "Tesla",
        "model": "Model 3",
        "category": "Electric",
        "price": 45000.0,
        "quantity": 4
    })
    vehicle_id = create_response.json()["id"]
    
    # Delete the vehicle
    response = client.delete(f"/api/vehicles/{vehicle_id}")
    assert response.status_code == 200
    
    # Verify it's deleted
    get_response = client.get(f"/api/vehicles/{vehicle_id}")
    assert get_response.status_code == 404


def test_search_vehicles_by_make(client):
    """Test searching vehicles by make"""
    client.post("/api/vehicles", json={
        "make": "Nissan",
        "model": "Altima",
        "category": "Sedan",
        "price": 24000.0,
        "quantity": 3
    })
    
    response = client.get("/api/vehicles/search?make=Nissan")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert data[0]["make"] == "Nissan"


def test_search_vehicles_by_price_range(client):
    """Test searching vehicles by price range"""
    client.post("/api/vehicles", json={
        "make": "Mazda",
        "model": "CX-5",
        "category": "SUV",
        "price": 28000.0,
        "quantity": 2
    })
    
    response = client.get("/api/vehicles/search?min_price=20000&max_price=30000")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_purchase_vehicle(client):
    """Test purchasing a vehicle (decreases quantity)"""
    create_response = client.post("/api/vehicles", json={
        "make": "Volkswagen",
        "model": "Jetta",
        "category": "Sedan",
        "price": 20000.0,
        "quantity": 5
    })
    vehicle_id = create_response.json()["id"]
    
    response = client.post(f"/api/vehicles/{vehicle_id}/purchase", json={"quantity": 2})
    assert response.status_code == 200
    data = response.json()
    assert data["quantity"] == 3


def test_purchase_more_than_available(client):
    """Test purchasing more vehicles than available"""
    create_response = client.post("/api/vehicles", json={
        "make": "Subaru",
        "model": "Outback",
        "category": "SUV",
        "price": 27000.0,
        "quantity": 2
    })
    vehicle_id = create_response.json()["id"]
    
    response = client.post(f"/api/vehicles/{vehicle_id}/purchase", json={"quantity": 5})
    assert response.status_code == 400


def test_restock_vehicle(client):
    """Test restocking a vehicle (increases quantity)"""
    create_response = client.post("/api/vehicles", json={
        "make": "Hyundai",
        "model": "Elantra",
        "category": "Sedan",
        "price": 19000.0,
        "quantity": 2
    })
    vehicle_id = create_response.json()["id"]
    
    response = client.post(f"/api/vehicles/{vehicle_id}/restock", json={"quantity": 3})
    assert response.status_code == 200
    data = response.json()
    assert data["quantity"] == 5
