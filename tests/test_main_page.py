class TestMainPage:

    def test_page_has_title(self, main_page):
        main_page.open()
        assert main_page.get_title() == "The Internet"

    def test_page_has_fork_me_element(self, main_page):
        main_page.open()
        assert main_page.get_fork_me_element().is_visible()

    def test_page_contains_44_links(self, main_page):
        main_page.open()
        assert main_page.get_content_links_count() == 44