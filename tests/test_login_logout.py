class TestLoginLogout:
    """Scenario 3: Full login/logout flow."""

    USERNAME = "tomsmith"
    PASSWORD = "SuperSecretPassword!"

    def test_full_login_logout_flow(self, login_page, secure_page):
        # Open Login page and login
        login_page.open()
        login_page.login(self.USERNAME, self.PASSWORD)

        # Assert user is on /secure page
        assert "/secure" in secure_page.get_current_url()

        # Assert page has title and content
        assert secure_page.get_page_title_text() == "Secure Area"
        assert secure_page.get_page_content().is_visible()

        # Assert page has Logout button
        assert secure_page.get_logout_button().is_visible()

        # Logout
        secure_page.click_logout()

        # Assert user is logged out
        assert "/login" in login_page.get_current_url()
        flash_text = login_page.get_flash_message_text()
        assert "logged out" in flash_text.lower()