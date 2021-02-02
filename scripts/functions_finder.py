from src.ui import main_ui
from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtCore import Qt
import sys
# import os
import pydoc

sys.path += \
    ['C:\\Program Files\\Autodesk\\Maya2016.5\\'
     'Python\\Lib\\site-packages\\pymel']


def get_installed_packages():
    import pkgutil
    packages = list()
    package_list = pkgutil.iter_modules()
    for each in package_list:
        packages.append(each[1])
    return packages


INSTALLED_PACKAGES = get_installed_packages()


def my_fun(e):
    return e.lower()


def help_fun(fun_str):
    return pydoc.plain(pydoc.render_doc(fun_str))


class BColors:
    def __init__(self):
        pass

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class QListWidget(QtWidgets.QListWidget):

    def __init__(self):
        super(QListView, self).__init__()

    def mousePressEvent(self, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            if event.button() == QtCore.Qt.LeftButton:
                super(QListView, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.type() == QtCore.QEvent.MouseButtonRelease:
            if event.button() == QtCore.Qt.LeftButton:
                super(QListView, self).mouseReleaseEvent(event)


X = 0
X2 = 0  # !!!!
Y = 0
Y2 = 0  # !!!!


class FunctionFinderTool(main_ui.MainWindow, QtWidgets.QMainWindow):
    leftClick = True

    def __init__(self):
        super(FunctionFinderTool, self).__init__()
        self.setupUi(self)
        self.connect_function_finder_tool()
        self.help_display_text_box.setReadOnly(True)

        # Set frame-less window

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        # Resize Window

        layout = QtWidgets.QVBoxLayout()
        sizegrip = QtWidgets.QSizeGrip(self)
        layout.addWidget(sizegrip, 0,
                         QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.setLayout(layout)

        # Movable Window

        self.oldPos = self.pos()

        self.center()
        self.add_items()

    def close_window(self):
        self.close()

    def minimise_window(self):
        self.showMinimized()

    def maximise_window(self):
        if not self.isMaximized():
            self.showMaximized()
        else:
            self.setWindowState(Qt.WindowNoState)

    def mouseMoveEvent(self, event):
        super(FunctionFinderTool, self).mouseMoveEvent(event)

        if self.leftClick:
            self.move(
                event.globalPos().x() - X - X2,
                event.globalPos().y() - Y - Y2
            )

    def mousePressEvent(self, event):
        super(FunctionFinderTool, self).mousePressEvent(event)
        global X, Y, X2, Y2
        if event.button() == QtCore.Qt.LeftButton:
            self.leftClick = True
            X = event.pos().x()
            Y = event.pos().y()

    def mouseReleaseEvent(self, event):
        super(FunctionFinderTool, self).mouseReleaseEvent(event)
        self.leftClick = True

    def center(self):
        frame_geometry = self.frameGeometry()
        center = QtWidgets.QApplication.desktop().availableGeometry().center()
        frame_geometry.moveCenter(center)
        self.move(frame_geometry.topLeft())

    def connect_function_finder_tool(self):

        self.textBoxA.returnPressed.connect(self.add_items)
        self.backBtn.clicked.connect(self.back_btn_cc)
        self.list_widget.itemDoubleClicked.connect(self.listbox_doubleclick_cmd)
        self.searchTextBox.textChanged.connect(self.add_items_search)
        self.help_button.clicked.connect(self.print_help_fun)
        self.btn_close.clicked.connect(self.close_window)
        self.btn_minimize.clicked.connect(self.minimise_window)
        self.btn_maximize_restore.clicked.connect(self.maximise_window)

    def mousePressEvent(self, event):
        """
        re-implemented to suppress Right-Clicks from selecting items.
        Args:
            event:

        Returns:

        """

        if event.type() == QtCore.QEvent.MouseButtonPress:
            if event.button() == QtCore.Qt.RightButton:
                return "RightClick Pressed"
            else:
                return "LeftClick"

    def add_items_search(self):
        self.list_widget.clear()
        current_function = self.textBoxA.text()
        list_index = 0
        if current_function:
            check = current_function.split(".")
            exec("import " + str(check[0]))
            for e in dir(eval(current_function)):
                if str(self.searchTextBox.text().lower()) in e.lower():
                    self.list_widget.insertItem(list_index, e)
                    list_index = list_index + 1
        else:
            if self.searchTextBox.text() == "":
                self.empty_text_command()
            else:
                for e in INSTALLED_PACKAGES:
                    if str(self.searchTextBox.text().lower()) in e.lower():
                        self.list_widget.insertItem(list_index, e)
                        list_index = list_index + 1

    def add_items(self):

        self.list_widget.clear()
        if self.textBoxA.text() == "":
            self.empty_text_command()

        else:
            current_function = self.textBoxA.text()

            check = current_function.split(".")
            exec("import " + str(check[0]))

            list_index = 0
            for e in dir(eval(current_function)):
                self.list_widget.insertItem(list_index, e)
                list_index = list_index + 1

    def back_btn_cc(self):
        current_function = str(self.textBoxA.text())
        check = current_function.split(".")
        final_cmd = ""

        if len(check) != 1:
            for each in check:
                if each != check[len(check) - 1]:
                    final_cmd = (final_cmd + each + ".")
                else:
                    final_cmd = final_cmd[:-1:]
            exec("import " + str(check[0]))
            # current = eval(final_cmd)
            self.textBoxA.setText(final_cmd)

        else:
            self.textBoxA.setText("")

        self.add_items()

    def listbox_doubleclick_cmd(self):

        fun_name = self.list_widget.currentItem().text()

        if self.textBoxA.text() == "":
            self.textBoxA.setText(fun_name)
            exec("import " + fun_name)

        else:
            self.textBoxA.setText(self.textBoxA.text() + "." + fun_name)
            fun_name_b = self.textBoxA.text()
            check = fun_name_b.split(".")
            print(check)
            exec("import " + str(check[0]))

        self.add_items()

    def empty_text_command(self):
        base_package_list = [
            "spider", "os", "random", "imath", "math",
            "PySide", "sys", "ix", "json"
        ]
        base_package_list = INSTALLED_PACKAGES + base_package_list
        base_package_list.sort(key=my_fun)
        list_index = 0
        for e in base_package_list:
            self.list_widget.insertItem(list_index, e)
            list_index = list_index + 1

    def print_help_fun(self):
        print(self.mousePressEvent)
        fun_name = self.list_widget.currentItem().text()
        text_box = self.help_display_text_box

        if self.textBoxA.text() != "":
            # Clearing the Existing Text Box
            text_box.setPlainText("")

            classpath = (self.textBoxA.text() + "." + fun_name)
            current_function = self.textBoxA.text()
            check = current_function.split(".")
            exec("import " + str(check[0]))

            text_box.appendPlainText("Current Function : "
                                     + str(classpath) + "\n")
            text_box.appendPlainText(str(help_fun(eval(classpath))))
            text_box.appendPlainText(
                "--------------------------------"
                + "end of help" +
                "--------------------------------")
            self.help_display_text_box.setTextCursor(0)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    fb = FunctionFinderTool()
    fb.show()
    app.exec_()
