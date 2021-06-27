import configparser

#DATABASE CONFIGURATION SCOPE
config =configparser.RawConfigParser()
with open('Application/app_config.ini', 'r', encoding='utf-8') as f:
    config.read_file(f)
    db_config = {
        'login':config['DATABASE']['login'],
        'password':config['DATABASE']['password'],
        'url':config['DATABASE']['url'],
        'database':config['DATABASE']['db']
    }


# DB_URL = 'mysql://{user}:{password}@{url}/{db}'.format(
#     user=db_config['login'], password=db_config['password'], url=db_config['url'], db=db_config['database'])


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False
    ASSETS_DEBUG = False


class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
    TESTING = False
    # USE_X_SENDFILE = True # ?


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    TESTING = True
    SEND_FILE_MAX_AGE_DEFAULT = 0  # forbid caching
    TEMPLATES_AUTO_RELOAD = True


class TestConfig(Config):
    ENV = 'testing'
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False