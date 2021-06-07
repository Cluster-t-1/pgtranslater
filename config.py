import os

isProduction = True

postgresConfig = {
    "user": "postgres",
    "password": "123" if isProduction else "123",
    "host": "localhost",
    "dbName": "dbName"
}


class FlaskConfig:

    DEBUG = not isProduction

    PROPAGATE_EXCEPTIONS = True
    SECRET_KEY = "моего деда съели дворфы"

    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@{host}/{dbName}'.format(**postgresConfig)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'testm3288@gmail.com'
    MAIL_PASSWORD = 'mytest123456789'


serverHost = 'localhost'
serverPort = os.environ.get("PORT", 5000)

langs = ['ru', 'ro', 'en']

# backendAddress = "https://teatru-server.itways.org" if isProduction else f"http://{serverHost}:{serverPort}"
# frontendAddress = "https://teatru-client.itways.org" if isProduction else "http://localhost:4200"

logsAuthUserName = "admin001"  # /logs
logsAuthPassword = "001"
