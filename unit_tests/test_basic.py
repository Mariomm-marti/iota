import iota
from fastapi.testclient import TestClient


def test_main():
    test_client = TestClient(iota.app)

    assert test_client.get("/").json() == {
        "status": "OK",
        "app": "iota",
        "repository": "https://github.com/Mariomm-marti/iota",
        "version": iota.VERSION,
        "request_count": 1,
    }

    assert test_client.get("/").json() == {
        "status": "OK",
        "app": "iota",
        "repository": "https://github.com/Mariomm-marti/iota",
        "version": iota.VERSION,
        "request_count": 2,
    }


def test_health():
    test_client = TestClient(iota.app)

    test_client.get("/")
    assert test_client.get("/health").status_code == 500
    test_client.get("/")
    assert test_client.get("/health").status_code == 200
