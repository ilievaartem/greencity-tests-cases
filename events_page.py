from selenium.webdriver.common.by import By
from base_page import BasePage

class EventsCardComponent:
    def __init__(self, root_element, base_page_instance):
        self.root = root_element
        self.page = base_page_instance

        self.MORE_BUTTON = (By.XPATH, ".//button[contains(@class, 'secondary-global-button') and contains(text(), 'Більше')]")
    
    def click_more(self):
        btn = self.root.find_element(*self.MORE_BUTTON)
        self.page.js_click(btn)
    
class EventsPage(BasePage):
    URL = "https://www.greencity.cx.ua/#/greenCity/events"

    BACK_BUTTON = (By.XPATH, "//div[ contains(@class, 'button-text') or contains(text(), 'Повернутися')]")
    SEARCH_ICON = (By.CSS_SELECTOR, "span.search-img")
    SEARCH_INPUT = (By.XPATH, "//input[@type='text' or contains(@class, 'place-input') or contains(@class, 'search')]")
    CLEAR_SEARCH_BTN = (By.CSS_SELECTOR, "span.close-icon, img.cross-icon, .close-icon, .cross-position")
    NO_RESULTS_MESSAGE = (By.XPATH, "//*[contains(text(), 'Ми не знайшли жодних результатів, що відповідають цьому запиту') or contains(@class, 'end-page-txt')]")

    EVENT_CARD = (By.XPATH, "//div[contains(@class, 'event-card')]")
 
    def open(self):
        self.driver.get(self.URL)

    def get_first_event_card(self):
        card_element = self.wait_for_element_visible(self.EVENT_CARD)
        return EventsCardComponent(card_element, self)

    def click_search_icon(self):
        self.wait_for_element_clickable(self.SEARCH_ICON).click()

    def search_for_event(self, text):
        input_element = self.wait_for_element_visible(self.SEARCH_INPUT)
        input_element.send_keys(text)

    def clear_search(self): 
        self.wait_for_element_clickable(self.CLEAR_SEARCH_BTN).click()

    def get_search_input_value(self):
        return self.wait_for_element_visible(self.SEARCH_INPUT).get_attribute("value")

    def get_event_title_by_text(self, text):
        return self.wait_for_element_visible((By.XPATH, f"//p[contains(@class, 'event-name') and contains(text(), '{text}')]")).text    
    
    def is_no_results_message_displayed(self):   
        return self.wait_for_element_visible(self.NO_RESULTS_MESSAGE).is_displayed
    
    def is_back_button_displayed(self):
        return self.wait_for_element_visible(self.BACK_BUTTON).is_displayed()
    