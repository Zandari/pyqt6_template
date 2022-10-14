from PyQt6 import QtWidgets, QtCore
from .templates.UiMainWidget import Ui_Form


class MainWidget(QtWidgets.QWidget):
    signal = QtCore.pyqtSignal(int)

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.setWindowTitle("Clicker")
        self._ui = Ui_Form()
        self._ui.setupUi(self)
        self._ui.pushButton.clicked.connect(self._button_clicked)

        self._counter = 0

    def _button_clicked(self):
        self._counter += 1
        self._ui.label.setText(str(self._counter))
        self.signal.emit(self._counter)
