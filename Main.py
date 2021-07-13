from controler.FileManager import FileManager
from interface.CLI import CLI


def init():
    fileManager = FileManager()
    fileManager.creatNeedFolder()

init()
CLI().start()
