class BaseConfig:
    """ Base Configuration"""
    TESTING = False


class DevelopmentConfig(BaseConfig):
    """Development Configuration"""
    pass


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True


class ProductionConfig(BaseConfig):
    pass

