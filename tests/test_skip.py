import pytest
from selene import browser, have

size_windows_1 = [(1980, 1080,),
                  (1600, 1200,),
                  (1280, 960,),
                  (428, 900,),
                  (372, 812,),
                  (414, 896,)]


@pytest.fixture(params=size_windows_1)
def size_windows(request):
    return request.param


def test_desktop(size_windows):
    browser.driver.set_window_size(size_windows[0], size_windows[1])
    if size_windows[0] > 900:
        browser.element('a[href$="/login"]').click()
        browser.element('#login div h1').should(have.text('Sign in to GitHub'))
        browser.element('#login_field').click().send_keys('lasha.bas@mail.ru')
        pytest.skip(reason='Skip mobile')


def test_mobile(size_windows):
    browser.driver.set_window_size(size_windows[0], size_windows[1])
    if size_windows[0] < 900:
        browser.element('button .Button-label').click()
        browser.element("a[href^='/login']").click()
        browser.element("input[name='login']").send_keys('lasha@mail.ru')
        pytest.skip(reason='skip mobile')

