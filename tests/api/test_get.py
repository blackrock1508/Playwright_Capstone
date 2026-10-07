from typing import TypedDict
from venv import logger

from playwright.sync_api import Playwright
import pytest
from typing import TypedDict,Dict 

import logging
from pathlib import Path



logfolder = Path("logs")
logfolder.mkdir(exist_ok=True)
logfile = logfolder / "api.log"
logger= logging.getLogger("LoginTestLogger")
logger.setLevel(logging.INFO)
logger.propagate = False
handler = logging.FileHandler(logfile, mode='a')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)   

class User(TypedDict):
    id: int
    name: str
    username: str
    email: str
    address: Dict
    phone: str
    website: str
    company: Dict


def test_get_users(playwright: Playwright):
    request_context = playwright.request.new_context()
    response = request_context.get("https://jsonplaceholder.typicode.com/users")
    assert response.status == 200

    users: list[User] = response.json()

    # Find user by business value (name)
    user = next(
        (u for u in users if u["name"] == "Leanne Graham"),
        None
    )

    # Validate user exists
    assert user is not None

    # Validate another property
    assert user["email"] == "Sincere@april.biz"