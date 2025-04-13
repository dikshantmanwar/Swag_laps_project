from configparser import ConfigParser

config = ConfigParser()
config.read(
    "C:\\Users\\Admin\\PycharmProjects\\Swag_Labs_Project\\Configuration\\config.ini"
)


class ReadValue:
    @staticmethod
    def getusername():
        username = config.get("login_info", "username")
        return username

    @staticmethod
    def invalidgetusername():
        invalidusername = config.get("login_info", "invalidusername")
        return invalidusername
    @staticmethod
    def getPassword():
        password = config.get("login_info", "passwords")
        return password

    @staticmethod
    def invalidgetPassword():
        invalidpassword = config.get("login_info", "invalidpasswords")
        return invalidpassword

    @staticmethod
    def getUrl():
        URL = config.get("login_info", "url")
        return URL
