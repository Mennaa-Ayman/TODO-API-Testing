# TODO API Testing

API testing for the `/todos` endpoint using the public JSONPlaceholder API. This project demonstrates testing REST APIs with both **Python (pytest)** and **Postman**.

## Project Structure

```
|
├── tests/
│   ├── test_todos_api.py     # Tests for /todos endpoint
│   └── conftest.py           # Pytest fixtures & configuration
│
├── Postman/
│   ├── Collection/
│   │   └── Postman_Collection.postman_collection.json
│   └── Environment/
│       └── TestEnv.postman_environment.json
│
├── pytest.ini                # Pytest discovery and markers
├── Requirements.txt          # Python dependencies
└── README.md                 
```

## What's Tested

| Test | HTTP Method | Purpose |
|------|------------|---------|
| `test_get_all_todos` | GET /todos | Fetch all todos |
| `test_get_todo_schema` | GET /todos/{id} | Fetch 3 todos (ids: 1,5,10); validate types |
| `test_post_todo` | POST /todos | Create new todo; check response has id |
| `test_put_todo` | PUT /todos/{id} | Full replace of a todo |
| `test_patch_todo` | PATCH /todos/{id} | Partial update (title only) |
| `test_delete_todo` | DELETE /todos/{id} | Delete a todo |

## How to Run

### Using Python (pytest)

**1. Install dependencies:**
```bash
pip install -r Requirements.txt
```

**2. Run the tests:**
```bash
pytest
```

**3. Generate an HTML report:**
```bash
pytest --html=report.html --self-contained-html
```

### Using Postman

**1. Import the collection and environment:**
   - Open Postman
   - Import `Postman/Collection/Postman_Collection.postman_collection.json`
   - Import `Postman/Environment/TestEnv.postman_environment.json`

**2. Select the environment:**
   - In Postman, select `TestEnv` from the environment dropdown

**3. Run the requests:**
   - Execute individual requests or use the Collection Runner to run all requests


