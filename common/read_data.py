import yaml
import json
from configparser import ConfigParser
from common.logger import logger


class MyConfigParser(ConfigParser):
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    # 重写configparser中的optionxform函数，解决.ini文件中的键option自动转为小写的问题
    def optionxform(self, optionstr):
        return optionstr


class ReadFileData():
    def __init__(self):
        pass

    def load_yml(self, file_path):
        logger.info("加载{}文件...".format(file_path))
        with open(file_path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        logger.info("读到数据 ==>> {}".format(data))
        return data

    def load_json(self, file_path):
        logger.info("加载{}文件...".format(file_path))
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        logger.info("读到数据 ==>> {}".format(data))
        return data

    def load_ini(self, file_path):
        logger.info("加载{}文件...".format(file_path))
        config = MyConfigParser()
        config.read(file_path, encoding="UTF-8")
        data = dict(config._sections)
        return data


data = ReadFileData()
