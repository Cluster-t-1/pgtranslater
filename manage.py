from settings import manager
# from models.adminUser import AdminUser
# from models.page import Page

if __name__ == '__main__':
    manager.run()

# export FLASK_APP=manage.py
# Инициализация:            flask db init
# Подготовка к миграции:    flask db migrate
# Миграция:                 flask db upgrade
