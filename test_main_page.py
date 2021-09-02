from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"

def goto_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()

def test_guest_can_goto_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.goto_login_page()