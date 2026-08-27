from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from login_page import LoginPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area" in login_page.get_flash_message()


def test_invalid_login_shows_error(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("wronguser", "wrongpassword")
    assert "Your username is invalid" in login_page.get_flash_message()