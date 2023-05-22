import pytest
from selene import browser


@pytest.fixture(autouse=True)
def browser_open():
    browser.config.base_url='https://github.com'
    yield
    browser.quit()