import unittest
from selenium import webdriver
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from events_page import EventsPage

class GreenCityEventsTests(unittest.TestCase):
    
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=options)  
        self.driver.maximize_window()
        self.page = EventsPage(self.driver)
        self.page.open()
        
    def tearDown(self):
        self.driver.quit()

    def test_open_event_details(self):
        first_event_card = self.page.get_first_event_card()

        first_event_card.click_more()

        self.assertTrue(self.page.is_back_button_displayed(), "Після відкриття деталей події кнопка 'Повернутися' не відображається.")

    def test_search_exact_event(self):
        search_query = "123123"

        self.page.click_search_icon()
        self.page.search_for_event(search_query)

        first_result_title = self.page.get_event_title_by_text(search_query)   
        self.assertIn(search_query, first_result_title, f"Після пошуку '{search_query}' перша знайдена подія не містить цей текст.")

        self.page.clear_search()
        self.assertEqual(self.page.get_search_input_value(), "", "Після очищення пошукового поля воно не є порожнім.")

    def test_search_invalid_query(self):
        invalid_query = "asdasdasd"

        self.page.click_search_icon()
        self.page.search_for_event(invalid_query)

        self.assertTrue(self.page.is_no_results_message_displayed(), f"Після пошуку '{invalid_query}' не відображається повідомлення про відсутність результатів.")

if __name__ == "__main__":
    unittest.main()