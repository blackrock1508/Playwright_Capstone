import logging
from pathlib import Path

from playwright.sync_api import Playwright

BASE_DIR = Path(__file__).resolve().parents[2]
logfolder = BASE_DIR / "logs"
logfolder.mkdir(exist_ok=True)
logfile = logfolder / "test_put.log"

logger = logging.getLogger("LoginTestLogger")
logger.setLevel(logging.INFO)
logger.propagate = False
handler = logging.FileHandler(logfile, mode="w")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

def test_put_api(playwright: Playwright):
    
    # Payload to update the resource
    payload = {
        "id": 1,
        "title": "Updated Title",
        "body": "Updated body content",
        "userId": 1
    }

    # PUT request
    request_context = playwright.request.new_context()

    response = request_context.put(
        "https://jsonplaceholder.typicode.com/posts/1",
        data=payload
    )

    # Status code check
    assert response.status == 200

    # JSON response
    data = response.json()

    # Validate updated fields
    assert data["id"] == 1
    assert data["title"] == "Updated Title"
    assert data["body"] == "Updated body content"
    assert data["userId"] == 1

    print("PUT Response:", data)
