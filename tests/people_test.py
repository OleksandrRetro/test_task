from http import HTTPStatus

from starlette.testclient import TestClient

from srv.main import srv

client = TestClient(srv)

ROUTE = "/people"


def test_get_all_peoples():
    response = client.get(ROUTE)
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) == 3


def test_get_first_people():
    response = client.get(f"{ROUTE}/1")
    assert response.status_code == HTTPStatus.OK
    assert response.json()["name"] == "Luke Skywalker"


def test_get_not_existed_people():
    response = client.get(f"{ROUTE}/1978")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json()["detail"] == "There are no info found."
