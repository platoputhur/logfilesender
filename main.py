#   MIT License
#   Copyright (c) 2021. Plato Puthur

import logging

from config.config import Configurator
from managers.email_manager import EmailManager
from managers.file_manager import FileManager


if __name__ == '__main__':
    config = Configurator.get_instance()
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.info("Reading the log file")
    file_content = FileManager.read_file(config.log_filepath)
    logging.info("Reading log file done.")
    logging.info('Attempting to send the email via smtp.')
    email_mgr = EmailManager.get_instance()
    email_mgr.send_mail(config.email_subject, file_content)
    logging.info('Sent the email via smtp.')
