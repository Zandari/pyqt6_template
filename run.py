import sys
import traceback
import logging
import os
from PyQt6 import QtWidgets
from datetime import datetime
from application import Application


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("error message:\n", tb)
    logging.info(tb)

    QtWidgets.QApplication.quit()


if __name__ == '__main__':
    # if not os.path.isdir("logs"):
    #     os.mkdir("logs")
    # cur_time = datetime.now().strftime("logging_%m_%d_%H_%M_%S")
    # logging.basicConfig(
    #     format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
    #     datefmt='%H:%M:%S',
    #     filename=f"logs\\{cur_time}.log",
    #     level=logging.DEBUG
    # )

    sys.excepthook = excepthook
    app = QtWidgets.QApplication(sys.argv)
    window = Application()
    app.setStyle('Fusion')
    app.exec()
