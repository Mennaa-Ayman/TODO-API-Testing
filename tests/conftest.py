import os
import pytest
import requests


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")


@pytest.fixture(scope="session")
def session() -> requests.Session:
    s = requests.Session()
    s.headers.update({"Content-Type": "application/json; charset=UTF-8"})
    yield s
    s.close()


@pytest.fixture(scope="session")
def todos_url(base_url: str) -> str:
    return f"{base_url}/todos"
