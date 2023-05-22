import pytest
from selene import browser


@pytest.fixture(autouse=True)
def browser_open():
    browser.open('https://github.com/')
    yield
    browser.quit()