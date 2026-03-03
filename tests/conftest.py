import os
import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.secure_page import SecurePage


@pytest.fixture()
def main_page(page, base_url) -> MainPage:
    return MainPage(page, base_url)


@pytest.fixture()
def login_page(page, base_url) -> LoginPage:
    return LoginPage(page, base_url)


@pytest.fixture()
def secure_page(page, base_url) -> SecurePage:
    return SecurePage(page, base_url)


@pytest.fixture()
def credentials():
    return {
        "username": os.getenv("TEST_USERNAME", "tomsmith"),
        "password": os.getenv("TEST_PASSWORD", "SuperSecretPassword!"),
    }