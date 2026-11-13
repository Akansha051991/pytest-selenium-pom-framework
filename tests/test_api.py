import pytest
from base.api_client import BaseApiClient

@pytest.fixture
def api_client():
    # Using a free public testing API base URL
    return BaseApiClient()

def test_get_users(api_client):
    # Send GET request to /users endpoint
    response = api_client.get("users")
    
    # Assertions
    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"
    data = response.json()
    assert len(data) > 0, "Users list is empty!"
    print(f"\n[INFO] Successfully fetched {len(data)} users via API.")

def test_create_post(api_client):
    # Send POST request to create a new resource
    payload = {
        "title": "Hybrid Automation Framework",
        "body": "Testing API layer inside Selenium Pytest project",
        "userId": 1
    }
    response = api_client.post("posts", payload=payload)
    
    # Assertions
    assert response.status_code == 201, f"Expected status 201, got {response.status_code}"
    response_data = response.json()
    assert response_data["title"] == "Hybrid Automation Framework"
    print(f"\n[INFO] Successfully created post with ID: {response_data.get('id')}")