import allure
from selenium.webdriver.common.by import By
from src.components.base_component import BaseComponent

class EventsCardComponent(BaseComponent):
    MORE_BUTTON = (By.XPATH, ".//button[contains(@class, 'secondary-global-button') and contains(text(), 'Більше')]")

    @allure.step("Клік на кнопку 'Більше' всередині картки події")
    def click_more(self):
        btn = self.find(self.MORE_BUTTON)
        self.page.js_click(btn)