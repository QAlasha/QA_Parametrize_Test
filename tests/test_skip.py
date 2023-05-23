import pytest
from selenium import webdriver
from selene import browser


@pytest.fixture(params=[(1920, 1080), (320, 240), (1600, 1200), (480, 360)],
                ids=['desktop', 'mobile', 'desktop', 'mobile'])
def web_browser(request):
    chrome_options = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_options
    browser.config.window_height = request.param[0]
    browser.config.window_width = request.param[1]

    if 'desktop' in request.node.name and 'mobile' in request.node.callspec.id:
        pytest.skip('Для теста не подходит мобильное соотношение сторон')
    elif 'mobile' in request.node.name and 'desktop' in request.node.callspec.id:
        pytest.skip('Для теста не подходит десктопное соотношение сторон')

    yield browser
    browser.quit()


@pytest.mark.desktop
def test_github_desktop(web_browser):
    browser.open('https://github.com/')
    browser.element('a.HeaderMenu-link--sign-in').click()


@pytest.mark.mobile
def test_github_mobile(web_browser):
    browser.open('https://github.com/')
    browser.element('.flex-column [aria-label="Toggle navigation"]').click()
    browser.element('a.HeaderMenu-link--sign-in').click()
