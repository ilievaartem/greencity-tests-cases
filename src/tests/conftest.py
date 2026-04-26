from selenium import webdriver
from src.data.config import Config
import pytest

@pytest.fixture(scope="function")
def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    if Config.HEADLESS_MODE:
        options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)  
    driver.maximize_window()
    
    yield driver

    driver.quit()