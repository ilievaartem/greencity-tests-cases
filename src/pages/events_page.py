import allure
from src.data.config import Config
from selenium.webdriver.common.by import By
from src.components.event_card_component import EventsCardComponent
from src.pages.base_page import BasePage
    
class EventsPage(BasePage):
    URL = Config.BASE_UI_URL

    BACK_BUTTON = (By.XPATH, "//div[ contains(@class, 'button-text') or contains(text(), 'Повернутися')]")
    SEARCH_ICON = (By.CSS_SELECTOR, "span.search-img")
    SEARCH_INPUT = (By.XPATH, "//input[@type='text' or contains(@class, 'place-input') or contains(@class, 'search')]")
    CLEAR_SEARCH_BTN = (By.CSS_SELECTOR, "span.close-icon, img.cross-icon, .close-icon, .cross-position")
    NO_RESULTS_MESSAGE = (By.XPATH, "//*[contains(text(), 'Ми не знайшли жодних результатів, що відповідають цьому запиту') or contains(@class, 'end-page-txt')]")

    EVENT_CARD = (By.XPATH, "//div[contains(@class, 'event-card')] | //*[contains(@class, 'event-list-item')] | //mat-card")
    # EVENT_CARD = (By.CSS_SELECTOR, "mat-card.event-list-item")
 
    @allure.step("Відкриття сторінки подій")
    def open(self):
        self.driver.get(self.URL)

    @allure.step("Отримання першої картки події з поточного списку")
    def get_first_event_card(self):
        card_element = self.wait_for_element_visible(self.EVENT_CARD)
        return EventsCardComponent(card_element, self)

    @allure.step("Клік на іконку пошуку")
    def click_search_icon(self):
        self.wait_for_element_clickable(self.SEARCH_ICON).click()

    @allure.step("Введення тексту в поле пошуку")
    def search_for_event(self, text):
        input_element = self.wait_for_element_visible(self.SEARCH_INPUT)
        input_element.send_keys(text)

    @allure.step("Очистка поля пошуку")
    def clear_search(self): 
        self.wait_for_element_clickable(self.CLEAR_SEARCH_BTN).click()

    @allure.step("Отримання поточного тексту в полі пошуку")
    def get_search_input_value(self):
        return self.wait_for_element_visible(self.SEARCH_INPUT).get_attribute("value")

    @allure.step("Отримання назви події за текстом в назві")
    def get_event_title_by_text(self, text):
        return self.wait_for_element_visible((By.XPATH, f"//p[contains(@class, 'event-name') and contains(text(), '{text}')]")).text    
    
    @allure.step("Перевірка відображення повідомлення про відсутність результатів")
    def is_no_results_message_displayed(self):   
        return self.wait_for_element_visible(self.NO_RESULTS_MESSAGE).is_displayed()
    
    @allure.step("Перевірка відображення кнопки 'Повернутися'")
    def is_back_button_displayed(self):
        return self.wait_for_element_visible(self.BACK_BUTTON).is_displayed()
    