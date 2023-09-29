import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def set_browser():
    browser.config.base_url = 'https://demoqa.com'
    #browser.config.window_width = 1920
    #browser.config.window_height = 1020
    #browser.config.driver.maximize_window()
    browser.config.timeout = 10

    yield

    browser.quit()