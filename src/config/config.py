import os
import yaml

from src.common import logger


class ConfigReader:
    @staticmethod
    def read_yml(path):
        try:
            with open(path) as stream:
                configs = yaml.load(stream, Loader=yaml.Loader)
                return configs
        except FileNotFoundError as e:
            logger.logger.error(f"Can not find config file: {e.filename}")
            return {}


class YMLConfig:

    def __init__(self, env, config_file_path=None):
        self.env = env
        self.config_file_path = config_file_path
        self.yml_config = self.get_yml_config()
        self.custom_config = {}

    def get_yml_config(self):
        if self.config_file_path is None or not os.path.isfile(self.config_file_path):
            return {}
        return ConfigReader.read_yml(self.config_file_path).get(self.env)

    def to_mapping(self):
        return {**self.yml_config, **self.custom_config}
