#   MIT License
#   Copyright (c) 2021. Plato Puthur

from smtplib import SMTP, SMTPConnectError, SMTPAuthenticationError
import ssl
from config.config import Configurator


class EmailManager:
    __instance__ = None

    @staticmethod
    def get_instance():
        """ Static access method """
        if EmailManager.__instance__ is None:
            EmailManager()
        return EmailManager.__instance__

    def __init__(self):
        if EmailManager.__instance__ is not None:
            raise Exception("Do not create multiple objects of this class")
        else:
            EmailManager.__instance__ = self
        self.config = Configurator.get_instance()

        if self.config.email_ssl == 'Yes':
            self.context = ssl.create_default_context()
        else:
            self.context = None

    def send_mail(self, subject, body):
        try:
            with SMTP(self.config.email_smtp_url, self.config.email_smtp_port) as email_server:
                email_server.starttls(context=self.context)
                email_server.login(self.config.email_username, self.config.email_password)
                message = """Subject: {subject} \
\n
{body}""".format(subject=subject, body=str(body))
                email_server.sendmail(self.config.email_username, self.config.to_email, message)
        except TimeoutError as te:
            print("Connection timed out! Error is: ", te)
        except SMTPConnectError as sce:
            print("Error occurred during the connection attempt. Error is: ", sce)
        except SMTPAuthenticationError as sae:
            print("Error occurred during the authentication attempt, probably the username/password combination is "
                  "wrong. Error is: ", sae)
