Проєкт: Автоматизація тестування GreenCity (POM + Components)
Цей репозиторій містить професійний фреймворк для автоматизованого UI-тестування модуля "Events" на платформі GreenCity. Проєкт побудований з використанням сучасних підходів до розробки тестового ПЗ.

🛠 Технологічний стек
Мова: Python 3.10+

Інструмент: Selenium WebDriver

Фреймворк: Pytest

Звітність: Allure Report

Паттерни: Page Object Model (POM) + Component-based approach

Конфігурація: python-dotenv (керування змінними через .env)

📂 Структура проєкту
greencity-tests/
├── src/
│   ├── components/        # UI Components (BaseComponent, EventCardComponent)
│   ├── data/              # Конфігурація (config.py, .env, env.example)
│   ├── pages/             # Page Objects (BasePage, EventsPage)
│   └── tests/             # Тест-кейси (Pytest) та фікстури
│       ├── conftest.py    # Фікстури (setup/teardown драйвера)
│       └── test_events_page.py 
├── test-cases/            # Ручні тест-кейси (Markdown)
├── .gitignore             # Файли, що ігноруються Git
├── pytest.ini             # Глобальні налаштування pytest та Allure
├── requirements.txt       # Залежності проєкту
└── README.md              # Документація

⚙️ Інструкція із запуску

1. Підготовка середовища
Клонуйте репозиторій та перейдіть у папку проєкту:

git clone <посилання-на-ваш-репозиторій>
cd greencity-tests
Створіть та активуйте віртуальне середовище:

python -m venv venv
# Windows (GitBash):
venv\Scripts\activate(source venv/Scripts/activate якщо термінал GitBash)
# Mac/Linux:
source venv/bin/activate
Встановіть необхідні бібліотеки:
pip install -r requirements.txt

2. Налаштування конфігурації
Створіть файл .env у папці src/data/ (використовуйте env.example як зразок). Додайте ваші дані:
BASE_UI_URL=https://www.greencity.cx.ua/#/greenCity/events
EXPLICIT_WAIT_TIMEOUT=15
HEADLESS_MODE=False

3. Запуск тестів
Щоб запустити всі тести та зібрати дані для звіту Allure:
pytest --alluredir=allure-result

4. Генерація звітів Allure
Після завершення тестів ви можете згенерувати та відкрити візуальний звіт:
allure serve allure-result

Особливості реалізації
BaseComponent: Усі UI-компоненти наслідуються від базового класу, що забезпечує єдину логіку пошуку елементів у межах конкретної ноди.

Allure Steps: Кожен метод сторінки та компонента анотований @allure.step, що робить звіти зрозумілими для не-технічних спеціалістів.

Стабільність: Використовуються виключно Explicit Waits (явні очікування) замість нестабільного time.sleep().

Ільєв Артем