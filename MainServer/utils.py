import os


def FilePath(file_list):
    pass


def FileExist(file_path):
    if os.path.exists(file_path):
        return True
    else:
        return False
