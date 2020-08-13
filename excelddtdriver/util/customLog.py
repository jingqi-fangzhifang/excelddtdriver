# _*_ coding:utf-8 _*_
"""自定义log"""
import logging
import datetime

"""自定义log"""


def getLogger(path):
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    handler = logging.FileHandler(path + now + "-log.txt")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


if __name__ == "__main__":
    getLogger("D:\\file\\pWorkSpace\\excelddtdriver\\log\\")
