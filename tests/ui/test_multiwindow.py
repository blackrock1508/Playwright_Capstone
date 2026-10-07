from playwright.sync_api import Page
from pathlib import Path


import pytest
import logging


logfolder = Path.cwd()/ "logs"
logfolder.mkdir(exist_ok=True)
logfile = logfolder / "test_multiwindow.log"
logger= logging.getLogger("MultiWindowTest")
logger.setLevel(logging.INFO)
logger.propagate = False
handler = logging.FileHandler(logfile, mode='a')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)




#logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s',filename='test_multiwindow.log',filemode='w')
#logger = logging.getLogger(__name__)

@pytest.mark.regression
def test_window(page: Page):
    # Navigate to the example page
    page.goto("https://demoqa.com/browser-windows")
    with page.expect_popup() as popup_info:
        page.get_by_role("button", name="New Window").first.click()
    new_page = popup_info.value
    new_page.wait_for_load_state("load")
    logger.info("new_page.url: %s", new_page.url)
    logger.error("page.url: %s", page.url)
    logger.info("Number of open pages: %s", len(page.context.pages))


for handler in logger.handlers:
    handler.flush()
     