import logging

from playwright.sync_api import Playwright
from trio import Path

from utils import json_utils

import logging


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

def test_api_deep_compare(playwright: Playwright):
    logger.info("Starting API deep compare test for user endpoint")
    request_context = playwright.request.new_context()
    response = request_context.get("https://jsonplaceholder.typicode.com/users/1")
    actual = response.json()
    logger.info("Fetched API response: %s", actual)

    expected = {
        "id": 1,
        "name": "Leanne Graham",
        "address": {
            "city": "Gwenborough"
        }
    }

    logger.info("Comparing actual payload to expected payload")
    mismatch = json_utils.deep_compare(actual, expected)
    logger.info("Deep compare result: %s", mismatch)
    assert mismatch is None, mismatch
