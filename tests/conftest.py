import pytest
from selene import browser

@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    browser.config.window_width = 1366
    browser.config.window_height = 705
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 20
    yield
    browser.quit()