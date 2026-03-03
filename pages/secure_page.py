from pages.base_page import BasePage


class SecurePage(BasePage):
    PATH = "/secure"

    # Locators
    LOGOUT_BUTTON = "a.button[href='/logout']"
    FLASH_MESSAGE = "#flash"
    PAGE_TITLE = "h2"
    PAGE_CONTENT = ".example"

    def get_page_title_text(self) -> str:
        return self.page.locator(self.PAGE_TITLE).inner_text()

    def get_page_content(self):
        return self.page.locator(self.PAGE_CONTENT)

    def get_logout_button(self):
        return self.page.locator(self.LOGOUT_BUTTON)

    def click_logout(self):
        self.get_logout_button().click()

    def get_flash_message_text(self) -> str:
        return self.page.locator(self.FLASH_MESSAGE).inner_text()