from typing import TypedDict
from venv import logger

from playwright.sync_api import Playwright
import pytest
from typing import TypedDict 

import logging
from pathlib import Path



logfolder = Path("logs")
logfolder.mkdir(exist_ok=True)
logfile = logfolder / "test_post.log"
logger= logging.getLogger("LoginTestLogger")
logger.setLevel(logging.INFO)
logger.propagate = False
handler = logging.FileHandler(logfile, mode='w')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)   

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
    logger.info(f"Response status code:{ respose.status}")
    logger.info(data)
    assert data["name"] == "John Doe"


    