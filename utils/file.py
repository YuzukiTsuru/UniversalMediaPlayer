import os
import time
from config import *


def make_dir(make_dir_path):
    path = make_dir_path.strip()
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def get_custom_log_file_name():
    file_name = 'ump-' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
    file_folder = os.path.abspath(os.path.dirname(__file__)) + os.sep + LOG_ROOT
    make_dir(file_folder)
    return file_folder + os.sep + file_name


def get_custom_fifo_file_name():
    file_name = "/tmp/ump_fifofile"
    file_folder = os.path.abspath(os.path.dirname(__file__)) + os.sep + LOG_ROOT
    make_dir(file_folder)
    return file_folder + os.sep + file_name
