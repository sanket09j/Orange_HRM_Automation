import logging
import os


class LogGen:

    @staticmethod
    def get_logger():

        project_path = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        log_folder = os.path.join(project_path, "Logs")

        # Create Logs folder if it does not exist
        os.makedirs(log_folder, exist_ok=True)

        log_path = os.path.join(
            log_folder,
            "automation.log"
        )

        logger = logging.getLogger()

        if not logger.hasHandlers():

            logger.setLevel(logging.INFO)

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )

            file_handler = logging.FileHandler(
                log_path,
                mode="a",
                encoding="utf-8"
            )

            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

        return logger