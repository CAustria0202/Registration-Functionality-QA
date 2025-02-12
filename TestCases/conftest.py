import os
import pytest
import configparser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ServiceChrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
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

    print(f"Selected browser: {browser}")
    print(f"Selected URL: {url}")
    return browser, url

@pytest.fixture(autouse=True)
def setup(request):
        browser, url = get_config()
        if browser == "chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--disable-notifications")
            driver = webdriver.Chrome(service=ServiceChrome(ChromeDriverManager().install()), options=chrome_options)
        elif browser == "firefox":
            firefox_options = webdriver.FirefoxOptions()
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