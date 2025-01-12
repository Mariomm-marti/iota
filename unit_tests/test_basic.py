import iota
from fastapi.testclient import TestClient
import pytest


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


def test_main_with_only_requests(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("SHOW_ONLY_REQUEST_COUNT", "true")
    test_client = TestClient(iota.app)

    assert test_client.get("/").json() == {
        "request_count": 3,
    }

    assert test_client.get("/").json() == {
        "request_count": 4,
    }

    monkeypatch.undo()


def test_health():
    iota.number_of_requests = 0
    test_client = TestClient(iota.app)

    test_client.get("/")
    assert test_client.get("/health").status_code == 500
    test_client.get("/")
    assert test_client.get("/health").status_code == 200
