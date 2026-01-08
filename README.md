# TODO API Testing

API testing setup against the `/todos` endpoint in the public JSONPlaceholder API.

## Project Structure

```
|
├── tests/
│   ├── test_todos_api.py     # CRUD tests for /todos endpoint
│   └── conftest.py           # Pytest fixtures & configuration
│
├── pytest.ini                # Pytest discovery and markers
├── Requirements.txt          # Python dependencies
└── README.md                 # Documentation
```

## How to Run

**1. Install dependencies:**
```bash
pip install -r Requirements.txt
pip install brotli  # Optional: suppress urllib3 warnings
```

**2. Run the tests:**
```bash
pytest
```

**3. Generate an HTML report:**
```bash
pytest --html=report.html --self-contained-html
```

## What's Tested

| Test | HTTP Method | Purpose |
|------|------------|---------|
| `test_list_todos_returns_list` | GET /todos | Fetch all todos |
| `test_get_todo_by_id_has_expected_schema` | GET /todos/{id} | Fetch 3 todos (ids: 1,5,10); validate types |
| `test_create_todo_returns_created_object` | POST /todos | Create new todo; check response has id |
| `test_update_todo_put_overwrites_fields` | PUT /todos/{id} | Full replace of a todo |
| `test_partial_update_todo_patch_updates_subset` | PATCH /todos/{id} | Partial update (title only) |
| `test_delete_todo_returns_success` | DELETE /todos/{id} | Delete a todo |
