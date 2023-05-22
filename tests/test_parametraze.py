from selene import browser, have
import pytest


@pytest.fixture(scope="function")
def size_browser(request):
    resolutions = {
        "desktop": (1920, 1080),
        "mobile": (428, 300)
    }
    return resolutions[request.param]


@pytest.mark.parametrize('size_browser', ['desktop'], indirect=True)
def test_desktop(size_browser):
    browser.driver.set_window_size(size_browser[0], size_browser[1])
    browser.element('a[href$="/login"]').click()
    browser.element('#login div h1').should(have.text('Sign in to GitHub'))
    browser.element('#login_field').click().send_keys('lasha.bas@mail.ru')


@pytest.mark.parametrize('size_browser', ['mobile'], indirect=True)
def test_mobile(size_browser):
    browser.driver.set_window_size(size_browser[0], size_browser[1])
    browser.element('button .Button-label').click()
    browser.element("a[href^='/login']").click()
    browser.element("input[name='login']").send_keys('lasha@mail.ru')
