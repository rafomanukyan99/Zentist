from pages.base_page import BasePage


class LoginPage(BasePage):
    PATH = "/login"

    # Locators
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "button[type='submit']"
    FLASH_MESSAGE = "#flash"

    def open(self):
        self.navigate(self.PATH)
        return self

    def login(self, username: str, password: str):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.locator(self.LOGIN_BUTTON).click()

    def get_flash_message_text(self) -> str:
        return self.page.locator(self.FLASH_MESSAGE).inner_text()

    def is_flash_error(self) -> bool:
        class_attr = self.page.locator(self.FLASH_MESSAGE).get_attribute("class")
        return class_attr is not None and "error" in class_attr