import pytest
from selenium import webdriver
import webdriver_manager.chrome


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(webdriver_manager.chrome.ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()
