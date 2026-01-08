import json
from typing import Dict

import pytest

# Testing all todos list
def test_get_all_todos(session, todos_url):
    resp = session.get(todos_url)
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    if data:
        item = data[0]
        for key in ("userId", "id", "title", "completed"):
            assert key in item

# Validates 3 todos datatypes
@pytest.mark.smoke
@pytest.mark.parametrize("todo_id", [1, 5, 10])
def test_get_todo_schema (session, todos_url, todo_id: int):
    resp = session.get(f"{todos_url}/{todo_id}")
    assert resp.status_code == 200
    data: Dict = resp.json()
    for key, typ in {"userId": int, "id": int, "title": str, "completed": bool}.items():
        assert key in data
        assert isinstance(data[key], typ)

# Post a new todo
def test_post_todo (session, todos_url):
    payload = {"userId": 1, "title": "Write tests", "completed": False}
    resp = session.post(todos_url, data=json.dumps(payload))
    # JSONPlaceholder typically returns 201 with an id, but allow 200/201
    assert resp.status_code in {200, 201}
    data = resp.json()
    for key in payload:
        assert key in data
    assert "id" in data

# Replace a todo
def test_put_todo (session, todos_url):
    todo_id = 1
    payload = {"userId": 1, "id": todo_id, "title": "Updated title", "completed": True}
    resp = session.put(f"{todos_url}/{todo_id}", data=json.dumps(payload))
    assert resp.status_code in {200, 201}
    data = resp.json()
    # Expect echoed data
    for k, v in payload.items():
        assert k in data
        assert data[k] == v

# Updates the title of a todo
def test_patch_todo (session, todos_url):
    todo_id = 1
    patch = {"title": "Patched title"}
    resp = session.patch(f"{todos_url}/{todo_id}", data=json.dumps(patch))
    assert resp.status_code in {200, 201}
    data = resp.json()
    assert "title" in data and data["title"] == patch["title"]

# Deletes a todo
def test_delete_todo (session, todos_url):
    todo_id = 1
    resp = session.delete(f"{todos_url}/{todo_id}")
    assert resp.status_code in {200, 204}
