import configparser
import os


class ConfigReader:

    config = configparser.ConfigParser()

    config_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "Config",
        "config.ini"
    )

    config.read(config_path)

    @classmethod
    def get_base_url(cls):
        return cls.config.get("DEFAULT", "base_url")

    @classmethod
    def get_browser(cls):
        return cls.config.get("DEFAULT", "browser")

    @classmethod
    def get_implicit_wait(cls):
        return cls.config.getint("DEFAULT", "implicit_wait")

    @classmethod
    def get_explicit_wait(cls):
        return cls.config.getint("DEFAULT", "explicit_wait")

    @classmethod
    def get_headless(cls):
        return cls.config.getboolean("DEFAULT", "headless")