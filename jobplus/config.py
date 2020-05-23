class BaseConfig(object):
    SECRET_KEY = 'ccdd-0126-5445887-522178852112/454651/efdx/1125'
class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost:3306/jobplus?charset=utf8'

class ProductionConfig(BaseConfig):
    pass

class TestingConfig(BaseConfig):
    pass

configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}