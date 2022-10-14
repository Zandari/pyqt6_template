from PyQt6 import QtCore
from gui.MainWidget import MainWidget


class Application(QtCore.QObject):
    def __init__(self, **kwargs):
        super(Application, self).__init__(**kwargs)
        self._main_widget = MainWidget()
        self._main_widget.signal.connect(self._main_widget_signal)
        self._main_widget.show()

    def _main_widget_signal(self, n: int):
        print(n)