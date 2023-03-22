from http import HTTPStatus

from starlette.testclient import TestClient

from srv.main import srv

client = TestClient(srv)

ROUTE = "/planets"


def test_get_all_planets():
    response = client.get(ROUTE)
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) == 3


def test_get_first_planet():
    response = client.get(f"{ROUTE}/1")
    assert response.status_code == HTTPStatus.OK
    assert response.json()["name"] == "Tatooine"


def test_get_not_existed_planet():
    response = client.get(f"{ROUTE}/34")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json()["detail"] == "There are no info found."
