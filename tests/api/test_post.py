from typing import TypedDict
from venv import logger

from playwright.sync_api import Playwright
import pytest
from typing import TypedDict 


class User(TypedDict):
    id: int
    name: str
    username: str
    email: str
    address: dict
    phone: str
    website: str
    company: dict   



@pytest.mark.api
def test_post_user(playwright: Playwright):
    request=playwright.request.new_context(base_url="https://jsonplaceholder.typicode.com/")
    payload = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "john.doe@example.com"
    }

    respose=request.post("/users", data=payload  )
    data=respose.json()
    assert respose.status==201
    logger.info("Response status code:", respose.status)
    logger.info(data)
    assert data["name"] == "John Doe"


    