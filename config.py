class Config:
    pass

class Development(Config):
    Debug = True

class Testing(Config):
    pass

config = {
    "development" : Development,
    "testing": Testing
}