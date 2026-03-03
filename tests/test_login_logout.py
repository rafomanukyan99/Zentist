class TestLoginLogout:
    """Scenario 3: Full login/logout flow."""

    def test_full_login_logout_flow(self, login_page, secure_page, credentials):
        # Open Login page and login
        login_page.open()
        login_page.login(credentials["username"], credentials["password"])

        # Assert user is on /secure page
        assert secure_page.get_current_url().endswith("/secure")

        # Assert page has title and content
        assert secure_page.get_page_title_text() == "Secure Area"
        assert secure_page.get_page_content().is_visible()

        # Assert page has Logout button
        assert secure_page.get_logout_button().is_visible()

        # Logout
        secure_page.click_logout()

        # Assert user is logged out
        assert "/login" in login_page.get_current_url()
        flash_text = login_page.get_flash_message_text().strip()
        assert "logged out" in flash_text.lower()