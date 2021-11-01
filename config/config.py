import configparser
import os


class Configurator:
    __instance__ = None

    @staticmethod
    def get_instance():
        if Configurator.__instance__ is None:
            Configurator()
        return Configurator.__instance__

    def __init__(self):
        if Configurator.__instance__ is not None:
            raise Exception("Do not create multiple objects of this class")
        else:
            Configurator.__instance__ = self
        config = configparser.ConfigParser()
        config.read("config/config.ini")
        config.sections()
        self.email_smtp_url = config['email']['smtp_url']
        self.email_ssl = config['email']['ssl']
        self.email_smtp_port = config['email']['smtp_port']
        self.email_username = config['email']['username']
        self.email_password = config['email']['password']
        self.email_subject = config['email']['subject']
        self.to_email = config['email']['to_email'].split(", ")
        self.log_filepath = config['log']['log_filepath']
