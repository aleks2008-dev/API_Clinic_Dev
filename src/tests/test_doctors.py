import json

import pytest

from app.api import crud


def test_create_doctor(test_app, monkeypatch):
    test_request_payload = {"name": "something", "surname": "something else"}
    test_response_payload = {"id": 1, "name": "something", "surname": "something else"}

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(crud, "post", mock_post)

    response = test_app.post("/doctors/", content=json.dumps(test_request_payload),)

    assert response.status_code == 201
    assert response.json() == test_response_payload


def test_create_doctor_invalid_json(test_app):
    response = test_app.post("/doctors/", content=json.dumps({"name": "something"}))
    assert response.status_code == 422

    response = test_app.post("/doctors/", content=json.dumps({"name": "1", "surname": "2"}))
    assert response.status_code == 422


def test_read_doctor(test_app, monkeypatch):
    test_data = {"id": 1, "name": "something", "surname": "something else"}

    async def mock_get(id):
        return test_data

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get("/doctors/1")
    assert response.status_code == 200
    assert response.json() == test_data


def test_read_doctor_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get("/doctors/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Doctor not found"

def test_read_all_doctors(test_app, monkeypatch):
    test_data = [
        {"name": "something", "surname": "something else", "id": 1},
        {"name": "someone", "surname": "someone else", "id": 2},
    ]

    async def mock_get_all():
        return test_data

    monkeypatch.setattr(crud, "get_all", mock_get_all)

    response = test_app.get("/doctors/")
    assert response.status_code == 200
    assert response.json() == test_data

def test_update_doctor(test_app, monkeypatch):
    test_update_data = {"name": "someone", "surname": "someone else", "id": 1}

    async def mock_get(id):
        return True

    monkeypatch.setattr(crud, "get", mock_get)

    async def mock_put(id, payload):
        return 1

    monkeypatch.setattr(crud, "put", mock_put)

    response = test_app.put("/doctors/1/", content=json.dumps(test_update_data))
    assert response.status_code == 200
    assert response.json() == test_update_data


@pytest.mark.parametrize(
    "id, payload, status_code",
    [
        [1, {}, 422],
        [1, {"surname": "bar"}, 422],
        [999, {"name": "foo", "surname": "bar"}, 404],
    ],
)
@pytest.mark.parametrize(
    "id, payload, status_code",
    [
        [1, {}, 422],
        [1, {"surname": "bar"}, 422],
        [999, {"name": "foo", "surname": "bar"}, 404],
        [1, {"name": "1", "surname": "bar"}, 422],
        [1, {"name": "foo", "surname": "1"}, 422],
        [0, {"name": "foo", "surname": "bar"}, 422],
    ],
)
def test_update_doctor_invalid(test_app, monkeypatch, id, payload, status_code):
    async def mock_get(id):
        return Doctor

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.put(f"/doctors/{id}/", content=json.dumps(payload),)
    assert response.status_code == status_code

def test_remove_doctor(test_app, monkeypatch):
    test_data = {"name": "something", "surname": "something else", "id": 1}

    async def mock_get(id):
        return test_data

    monkeypatch.setattr(crud, "get", mock_get)

    async def mock_delete(id):
        return id

    monkeypatch.setattr(crud, "delete", mock_delete)

    response = test_app.delete("/doctors/1/")
    assert response.status_code == 200
    assert response.json() == test_data


def test_remove_doctor_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return Doctor

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.delete("/doctors/999/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Doctor not found"

    response = test_app.delete("/doctors/0/")
    assert response.status_code == 422


def test_read_doctor_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get("/doctors/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Doctor not found"

    response = test_app.get("/doctors/0")
    assert response.status_code == 422