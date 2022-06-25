from selenium.webdriver.chrome.webdriver import WebDriver


def test_yandex_search():
    driver = WebDriver(executable_path='C://AllureChromeDriver//chromedriver.exe')
    driver.get('https://ya.ru')
    print(None)

