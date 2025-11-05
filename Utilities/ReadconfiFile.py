import configparser

config=configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def get_username():
        username = config.get("login_details","username")
        return username

    @staticmethod
    def get_password():
        password = config.get("login_details", "password")
        return password
