import json
import os
import sys
from configparser import ConfigParser

current_dir = os.getcwd()
__CURR_DIR = os.path.dirname(os.path.realpath(__file__))
PARENT_DIR = os.path.abspath(os.path.join(__CURR_DIR, os.pardir))
__PATH_TO_PYTEST_INI = os.path.abspath(os.path.join(__CURR_DIR, "pytest.ini"))

print(__CURR_DIR)
print(PARENT_DIR)
print(__PATH_TO_PYTEST_INI)

CONFIG_PARSER = ConfigParser()
# config parser variable used to access pytest.ini file.
CONFIG_PARSER.read(__PATH_TO_PYTEST_INI)
print(CONFIG_PARSER["pytest"]["addopts"])

CONFIG_PARSER.set("pytest", 'addopts', '-rA -vv -s -rf')
with open(__PATH_TO_PYTEST_INI, "w", encoding="utf-8") as update_cfg_parser:
    CONFIG_PARSER.write(update_cfg_parser)
print(CONFIG_PARSER["pytest"]["addopts"])
