from typing import TypedDict

from playwright.sync_api import Playwright
import pytest
from typing import TypedDict,Dict 
import logging
from pathlib import Path



logfolder = Path("logs")
logfolder.mkdir(exist_ok=True)
logfile = logfolder / "test_delete.log"
logger= logging.getLogger("LoginTestLogger")
logger.setLevel(logging.INFO)
logger.propagate = False
handler = logging.FileHandler(logfile, mode='w')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)   

class Post(TypedDict):
    id: int
    userId: int
    title: str
    body: str


def test_delete_api_typed(playwright: Playwright):
    request_context = playwright.request.new_context()
    # GET all posts
    res = request_context.get("https://jsonplaceholder.typicode.com/posts")
    posts: list[Post] = res.json()
    logger.info("Get All Posted data")
    # Find post by business value
    post = next((p for p in posts if p["title"].startswith("qui")), None)
    assert post is not None

    # DELETE that post
    del_res = request_context.delete(
        f"https://jsonplaceholder.typicode.com/posts/{post['id']}"
    )
    logger.info(f"Delete reposnse code:{del_res.status }")
    assert del_res.status == 200
