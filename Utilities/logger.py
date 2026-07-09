import logging
import os


class LogGen:

    @staticmethod
    def get_logger():

        log_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "Logs",
            "automation.log"
        )

        logger = logging.getLogger()

        if not logger.hasHandlers():

            logger.setLevel(logging.INFO)

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )

            file_handler = logging.FileHandler(log_path)

            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

        return logger