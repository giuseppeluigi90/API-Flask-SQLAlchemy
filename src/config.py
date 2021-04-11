class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://scx:y2K.scx@localhost/scxcp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development' : DevelopmentConfig
}
