from http import HTTPStatus

from starlette.testclient import TestClient

from srv.main import srv

client = TestClient(srv)

ROUTE = "/starships"


def test_get_all_starships():
    response = client.get(ROUTE)
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) == 3


def test_get_first_starship():
    response = client.get(f"{ROUTE}/1")
    assert response.status_code == HTTPStatus.OK
    assert response.json()["name"] == "CR90 corvette"


def test_get_not_existed_starship():
    response = client.get(f"{ROUTE}/100")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json()["detail"] == "There are no info found."
