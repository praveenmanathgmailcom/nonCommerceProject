import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get("common info", "baseurl")
        return url

    @staticmethod
    def getUserEmail():
        useremail = config.get("common info", "username")
        return useremail

    @staticmethod
    def getUserPassword():
        password = config.get("common info", "password")
        return password
