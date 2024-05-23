class Config:
    TESTING=False
    JSONIFY_PRETTYPRINT_REGULAR=True
    
class TestConfig(Config):
    TESTING=True

class DevConfig(Config):
    MYSQL_USER="root"
    MYSQL_PASSWORD="root"
    MYSQL_DB="db24centromedico"
    MYSQL_CURSORCLASS="DictCursor"

class ProdConfig(Config):
    MYSQL_USER="xx"
    MYSQL_PASSWORD="xx"
    MYSQL_DB="db24centromedicoprod"
    MYSQL_CURSORCLASS="DictCursor"

configDict={
    'development':DevConfig,
    'testing':TestConfig,
    'production':ProdConfig,
    'default':DevConfig
}