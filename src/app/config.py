class Config:
    SECRET_KEY = 'my secret..'

class TestingConfig(Config):
    TESTING =True
    pass
class DevelopmentConfig(Config):
    pass
class ProductionConfig(Config):
    pass
Config= {
    'testing':TestingConfig,
    'development':DevelopmentConfig,
    'production':ProductionConfig,
    'default': DevelopmentConfig
}