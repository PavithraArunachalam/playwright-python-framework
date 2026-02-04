from pages.login_page import LoginPage

def test_login_example(page):
    login_page = LoginPage(page)
    login_page.go_to_login_page("https://github.com/PavithraArunachalam/25th_Protfolio")
