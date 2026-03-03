import pytest


class TestLoginPageInvalidCredentials:
    """Scenario 2: Make sure it's impossible to login with invalid credentials."""

    VALID_USERNAME = "tomsmith"
    VALID_PASSWORD = "SuperSecretPassword!"

    @pytest.mark.parametrize(
        "username, password, description",
        [
            ("", "", "empty username and password"),
            ("tomsmith", "", "valid username, empty password"),
            ("", "SuperSecretPassword!", "empty username, valid password"),
            ("invaliduser", "SuperSecretPassword!", "invalid username, valid password"),
            ("tomsmith", "wrongpassword", "valid username, invalid password"),
            ("invaliduser", "wrongpassword", "both invalid"),
            ("TOMSMITH", "SuperSecretPassword!", "username wrong case"),
            ("tomsmith", "supersecretpassword!", "password wrong case"),
            (" tomsmith", "SuperSecretPassword!", "username with leading space"),
            ("tomsmith ", "SuperSecretPassword!", "username with trailing space"),
            ("tomsmith", " SuperSecretPassword!", "password with leading space"),
            ("tomsmith", "SuperSecretPassword! ", "password with trailing space"),
            ("tom smith", "SuperSecretPassword!", "username with space in middle"),
            ("admin", "admin", "common default credentials"),
            ("' OR 1=1 --", "password", "SQL injection attempt"),
        ],
    )
    def test_login_with_invalid_credentials(self, main_page, login_page, username, password, description):
        main_page.open()
        main_page.click_form_authentication()
        login_page.login(username, password)

        assert "/login" in login_page.get_current_url(), f"User left login page for: {description}"
        assert login_page.is_flash_error(), f"Expected error for: {description}"
        flash_text = login_page.get_flash_message_text().strip()
        assert "invalid" in flash_text.lower(), (
            f"Unexpected flash message for '{description}': {flash_text}"
        )