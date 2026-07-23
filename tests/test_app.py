from app import create_app


def test_home_page():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"AWS DevOps CI/CD Project" in response.data


def test_health_endpoint():
    app = create_app()
    client = app.test_client()

    response = client.get("/health")
    data = response.get_json()

    assert response.status_code == 200
    assert data["status"] == "healthy"
    assert data["service"] == "aws-devops-cicd-project"