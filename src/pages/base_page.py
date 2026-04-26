import allure
from src.data.config import Config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, Config.EXPLICIT_WAIT)

    @allure.step("Очікування видимості елемента")
    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step("Очікування клікабельності елемента")
    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    @allure.step("Клік за допомогою JavaScript")
    def js_click(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", element)