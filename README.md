# Проєкт: Автоматизація тестування сторінки подій GreenCity

Цей репозиторій містить автоматизовані UI-тести для модуля "Events" платформи GreenCity.
Тести реалізовані за допомогою **Python**, **Selenium WebDriver** та стандартного модуля **unittest** без використання сторонніх фреймворків.

### Посилання на сторінку тестування
[GreenCity Events](https://www.greencity.cx.ua/#/greenCity/events)

### Структура репозиторію
* `test-cases/events-page-tests.md` — ручні тест-кейси (Markdown).
* `tests/test_events_page.py` — скрипт з автоматизованими тестами.
* `requirements.txt` — залежності проєкту.
* `.gitignore` — файли, що ігноруються Git.

### Інструкція із запуску тестів

1. Клонуйте репозиторій:
    git clone <посилання-на-github>
2. Створіть та активуйте віртуальне середовище:
    python -m venv venv
    На Windows: venv\Scripts\activate(source venv/Scripts/activate якщо термінал GitBash)
    На Mac/Linux: source venv/bin/activate
3. Встановіть залежності:
    pip install -r requirements.txt
4. Запустіть тести за допомогою команди:
    python -m unittest discover tests

Ільєв Артем