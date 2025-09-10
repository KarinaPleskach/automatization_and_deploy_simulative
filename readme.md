
## Запуск проекта на новой машине

1. Скачайте проект:
   git clone https://github.com/KarinaPleskach/automatization_and_deploy_simulative.git
   cd automatization_and_deploy_simulative

2. Установите зависимости:
    pip install -r requirements.txt

3. Создайте базу данных в PostgreSQL:
    CREATE DATABASE sales_db;

4. В файле config.ini замените значения на свои:
    - логин
    - пароль
    - имя базы
    - хост
    - название таблицы

5. В файле start.bat и load.bat замените пути на свои:
    - путь к Python
    - путь к скрипту generate-sales-data.py
    - путь к скрипту load-data.py

6. Добавьте задачу в Планировщик Windows:
    - Откройте «Планировщик заданий»
    - Создайте задачу
    - В разделе «Триггеры» → укажите «Еженедельно», уберите воскресенье
    - В разделе «Действия» укажите запуск файла start.bat
    - То же с load.bat, только в «Триггеры» → укажите «Ежедневно»