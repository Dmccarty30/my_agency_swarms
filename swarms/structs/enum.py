from enum import Enum

class OutputTypeEnum(str, Enum):
    ALL = 'all'
    FINAL = 'final'
    LIST = 'list'
    DICT = 'dict'
    JSON = 'json'
    MD = '.md'
    TXT = '.txt'
    YAML = 'yaml'
    TOML = 'toml'
