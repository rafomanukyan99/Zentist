from pages.base_page import BasePage


class MainPage(BasePage):
    PATH = "/"

    # Locators
    FORK_ME_LINK = "img[alt='Fork me on GitHub']"
    CONTENT_LINKS = "#content ul li a"
    FORM_AUTH_LINK = "a[href='/login']"

    def open(self):
        self.navigate(self.PATH)
        return self

    def get_fork_me_element(self):
        return self.page.locator(self.FORK_ME_LINK)

    def get_content_links(self):
        return self.page.locator(self.CONTENT_LINKS)

    def get_content_links_count(self) -> int:
        return self.get_content_links().count()

    def click_form_authentication(self):
        self.page.locator(self.FORM_AUTH_LINK).click()