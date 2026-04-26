import allure
from src.pages.events_page import EventsPage

@allure.feature("Events Module")
@allure.story("Взаємодія зі сторінкою подій (Events Page)")
class TestGreenCityEvents:

    @allure.title("TC-01: Перевірка переходу на сторінку деталей події")
    def test_open_event_details(self, init_driver):
        page = EventsPage(init_driver)
        page.open()
        
        with allure.step("Отримання першої картки події та клік на кнопку 'Більше'"):
            first_event_card = page.get_first_event_card()
            first_event_card.click_more()

        with allure.step("Перевірка відображення кнопки 'Повернутися' на сторінці деталей події"):
            assert page.is_back_button_displayed() is True, "Після відкриття деталей події кнопка 'Повернутися' не відображається."

    @allure.title("TC-02: Перевірка функціональності пошуку подій")
    def test_search_exact_event(self, init_driver):
        search_query = "123123"
        page = EventsPage(init_driver)
        page.open()

        page.click_search_icon()
        page.search_for_event(search_query)

        with allure.step("Перевірка, що перша знайдена подія містить текст пошукового запиту"):
            result_text = page.get_event_title_by_text(search_query)   
            assert search_query in result_text, f"Після пошуку '{search_query}' перша знайдена подія не містить цей текст."

        page.clear_search()
        with allure.step("Очистка пошукового поля та перевірка, що воно порожнє"):
            assert page.get_search_input_value() == "", "Після очищення пошукового поля воно не є порожнім."

    @allure.title("TC-03: Перевірка пошуку з неіснуючим запитом")
    def test_search_invalid_query(self, init_driver):
        invalid_query = "asdasdasd"

        page = EventsPage(init_driver)
        page.open()
        
        page.click_search_icon()
        page.search_for_event(invalid_query)

        with allure.step("Перевірка відображення повідомлення про відсутність результатів після пошуку неіснуючого запиту"):
            assert page.is_no_results_message_displayed() is True, f"Після пошуку '{invalid_query}' не відображається повідомлення про відсутність результатів."
