import os
import pytest
import configparser
from selenium import webdriver
#Chrome Browser
from selenium.webdriver.chrome.service import Service as ServiceChrome
from webdriver_manager.chrome import ChromeDriverManager
#Chromium Browser
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.core.os_manager import ChromeType
#Firefox Browser
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
#Edge Browser
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def get_config():
    config = configparser.ConfigParser()

    # Get the path of the directory where conftest.py is located
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, "..", "config.ini")  # Adjust to go one level up to find config.ini

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found at: {config_path}")

    config.read(config_path)
    browser = config.get("settings", "browser", fallback="chrome")
    url = config.get("settings", "url", fallback="https://google.com/")
    head = config.getboolean("settings", "head", fallback=False)

    print(f"Selected browser: {browser}")
    print(f"Selected URL: {url}")
    print(f"Headless: {head}")
    return browser, url, head

@pytest.fixture(autouse=True)
def setup(request):
        browser, url, head = get_config()
        if browser == "chrome":
            chrome_options = webdriver.ChromeOptions()
            if head:
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--disable-gpu')
                chrome_options.add_argument('--window-size=1920,1080')
            driver = webdriver.Chrome(service=ServiceChrome(ChromeDriverManager().install()), options=chrome_options)
        elif browser == "chromium":
            chromium_options = webdriver.ChromeOptions()
            if head:
                chromium_options.add_argument('--headless')
                chromium_options.add_argument('--no-sandbox')
                chromium_options.add_argument('--disable-gpu')
                chromium_options.add_argument('--window-size=1920,1080')
            driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options=chromium_options)
        elif browser == "firefox":
            firefox_options = webdriver.FirefoxOptions()
            if head:
                firefox_options.add_argument('--headless')
                firefox_options.add_argument('--no-sandbox')
                firefox_options.add_argument('--disable-gpu')
                firefox_options.add_argument('--window-size=1920,1080')
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
        elif browser == "edge":
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        driver.get(url)
        driver.maximize_window()
        request.cls.driver = driver
        yield
        driver.quit()