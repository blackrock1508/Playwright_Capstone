from typing import TypedDict
from venv import logger

from playwright.sync_api import Playwright
import pytest
from typing import TypedDict 

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
