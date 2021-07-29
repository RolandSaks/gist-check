import json
import logging
import os
from typing import Any


class Configuration:
    PROPERTY_PATH_SEPARATOR = "."

    def __init__(self, source: str):
        self.source = source
        self.config = {}
        self.load()

    def load(self) -> None:
        try:
            with open(os.path.join(os.path.dirname(__file__), self.source), "r") as i:
                self.config = json.load(i)
        except FileNotFoundError:
            logging.error("Configuration file could not be loaded, source missing: " + self.source)

    def get_config(self) -> dict:
        return self.config

    def property(self, path: str) -> Any:
        value = self.config

        try:
            for prop in path.split(Configuration.PROPERTY_PATH_SEPARATOR):
                value = value[prop]
            return value
        except KeyError:
            logging.error("Unable to resolve configuration property: {}".format(path))
            return None

    def __str__(self):
        return str(self.config)
