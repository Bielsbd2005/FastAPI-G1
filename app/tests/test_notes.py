from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def login(username: str = "tester"):
    resp = client.post("/api/session/", json={"username": username})
    assert resp.status_code == 200
    return resp


def test_health():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"


def test_create_and_get_note():
    login()
    payload = {"title": "Test", "content": "This is a test note"}
    r = client.post("/api/notes/", json=payload)
    assert r.status_code == 201
    note = r.json()
    assert note["title"] == payload["title"]
    assert note["owner"] == "tester"
    note_id = note["id"]

    r2 = client.get(f"/api/notes/{note_id}")
    assert r2.status_code == 200
    assert r2.json()["content"] == payload["content"]


def test_list_notes():
    login()
    r = client.get("/api/notes/")
    assert r.status_code == 200
    assert isinstance(r.json(), list)


def test_update_note():
    login()
    # create
    payload = {"title": "To update", "content": "old"}
    r = client.post("/api/notes/", json=payload)
    note = r.json()
    nid = note["id"]

    # update
    new = {"title": "Updated", "content": "new content"}
    ru = client.put(f"/api/notes/{nid}", json=new)
    assert ru.status_code == 200
    assert ru.json()["title"] == "Updated"


def test_delete_note():
    login()
    # create
    payload = {"title": "To delete", "content": "bye"}
    r = client.post("/api/notes/", json=payload)
    note = r.json()
    nid = note["id"]

    rd = client.delete(f"/api/notes/{nid}")
    assert rd.status_code == 204

    # should be gone
    rg = client.get(f"/api/notes/{nid}")
    assert rg.status_code == 404
