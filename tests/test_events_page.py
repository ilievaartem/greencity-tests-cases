import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GreenCityEventsTests(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()  
        self.driver.maximize_window()
        self.driver.get("https://www.greencity.cx.ua/#/greenCity/events") 
        self.wait = WebDriverWait(self.driver, 10)
        
    def tearDown(self):
        self.driver.quit()

    def test_open_event_details(self):
        first_event_card = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'secondary-global-button') and contains(text(), 'Більше')][1]")))

        self.driver.execute_script("arguments[0].click();", first_event_card)

        back_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[ contains(@class, 'button-text') or contains(text(), 'Повернутися')]")))

        self.assertTrue(back_button.is_displayed(), "Після відкриття деталей події кнопка 'Повернутися' не відображається.")

    def test_search_exact_event(self):
        search_query = "123123"

        search_icon = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.search-img")))
        search_icon.click()

        search_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='text' or contains(@class, 'place-input') or contains(@class, 'search')]")))
        search_input.send_keys(search_query)

        first_result_title = self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//p[contains(@class, 'event-name') and contains(text(), '{search_query}')]")))

        self.assertIn(search_query, first_result_title.text, f"Після пошуку '{search_query}' перша знайдена подія не містить цей текст.")

        clear_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.close-icon, img.cross-icon, .close-icon, .cross-position")))
        clear_button.click()

        self.assertTrue(search_input.get_attribute("value") == "", "Після очищення пошукового поля воно не є порожнім.")

    def test_search_invalid_query(self):
        invalid_query = "asdasdasd"

        search_icon = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.search-img")))
        search_icon.click()

        search_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='text' or contains(@class, 'place-input') or contains(@class, 'search')]")))
        search_input.send_keys(invalid_query)

        no_results_message = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Ми не знайшли жодних результатів, що відповідають цьому запиту') or contains(@class, 'end-page-txt')]")))

        self.assertTrue(no_results_message.is_displayed(), f"Після пошуку '{invalid_query}' не відображається повідомлення про відсутність результатів.")

if __name__ == "__main__":
    unittest.main()