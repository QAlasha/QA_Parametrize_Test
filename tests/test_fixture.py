import pytest
from selene import browser, have


@pytest.fixture(params=[(1020, 1080), (1080, 1020)])
def web_desktop(request):
    browser.driver.set_window_size(request.param[0], request.param[1])


@pytest.fixture(params=[(600, 300), (300, 400)])
def web_mobile(request):
    browser.driver.set_window_size(request.param[0], request.param[1])


def test_desktop(web_desktop):
    browser.element('a[href$="/login"]').click()
    browser.element('#login div h1').should(have.text('Sign in to GitHub'))
    browser.element('#login_field').click().send_keys('lasha.bas@mail.ru')


def test_mobile(web_mobile):
    browser.element('button .Button-label').click()
    browser.element("a[href^='/login']").click()
    browser.element("input[name='login']").send_keys('lasha@mail.ru')
