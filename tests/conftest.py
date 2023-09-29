import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def set_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 10

    yield

    browser.quit()