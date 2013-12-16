from qtshim import QtGui, QtCore, Signal


def version1():
    """Very basic first version."""
    def create_window():
        win = QtGui.QMainWindow()
        return win

    if __name__ == '__main__':
        app = QtGui.QApplication([])
        win = create_window()
        win.show()
        app.exec_()
#version1()


def version2():
    """Shows creating textbox, layout, and central widget."""
    def create_window():
        # Create the widgets, starting with a window
        window = QtGui.QMainWindow()
        # Create a container that is parented to the window
        container = QtGui.QWidget(window)
        # Create a textbox that is parented to the container
        textbox = QtGui.QLineEdit(container)

        # Now, set up the layout.
        layout = QtGui.QHBoxLayout(container)
        container.setLayout(layout)
        layout.addWidget(textbox)
        window.setCentralWidget(container)

        # Return the window so it can be shown
        return window

    if __name__ == '__main__':
        app = QtGui.QApplication([])
        win = create_window()
        win.show()
        app.exec_()
#version2()

def version3():
    """Adds window title and multiple widgets."""

    def create_window():
        window = QtGui.QMainWindow()
        window.setWindowTitle('Hierarchy Converter')

        container = QtGui.QWidget(window)
        label = QtGui.QLabel('Prefix:', container)
        textbox = QtGui.QLineEdit(container)
        button = QtGui.QPushButton('Convert', container)

        layout = QtGui.QHBoxLayout(container)
        container.setLayout(layout)
        # Add them to the layout, first widget added is left-most
        layout.addWidget(label)
        layout.addWidget(textbox)
        layout.addWidget(button)
        window.setCentralWidget(container)

        return window

    if __name__ == '__main__':
        app = QtGui.QApplication([])
        win = create_window()
        win.show()
        app.exec_()
#version3()


def version4():
    """Adds convertClicked signal and support."""

    class ConverterWindow(QtGui.QMainWindow):
        convertClicked = Signal(str)

    def create_window():
        window = ConverterWindow()
        window.setWindowTitle('Hierarchy Converter')

        container = QtGui.QWidget(window)
        label = QtGui.QLabel('Prefix:', container)
        textbox = QtGui.QLineEdit(container)
        button = QtGui.QPushButton('Convert', container)

        def onclick():
            window.convertClicked.emit(textbox.text())
        button.clicked.connect(onclick)

        layout = QtGui.QHBoxLayout(container)
        container.setLayout(layout)
        layout.addWidget(label)
        layout.addWidget(textbox)
        layout.addWidget(button)
        window.setCentralWidget(container)

        return window

    if __name__ == '__main__':
        def onconvert(prefix):
            print 'Convert clicked! Prefix:', prefix
        app = QtGui.QApplication([])
        win = create_window()
        win.convertClicked.connect(onconvert)
        win.show()
        app.exec_()
#version4()

def version5():
    """Adds selection changed handling, controller, and status bar."""

    class HierarchyConverterController(QtCore.QObject):
        selectionChanged = Signal(list)

    class ConverterWindow(QtGui.QMainWindow):
        convertClicked = Signal(str)

    def create_window(controller):
        window = ConverterWindow()
        window.setWindowTitle('Hierarchy Converter')
        statusbar = window.statusBar()

        container = QtGui.QWidget(window)
        label = QtGui.QLabel('Prefix:', container)
        textbox = QtGui.QLineEdit(container)
        button = QtGui.QPushButton('Convert', container)

        def onclick():
            window.convertClicked.emit(textbox.text())
        button.clicked.connect(onclick)

        def onSelChanged(newsel):
            if not newsel:
                txt = 'Nothing selected.'
            elif len(newsel) == 1:
                txt = '%s selected.' % newsel[0]
            else:
                txt = '%s objects selected.' % len(newsel)
            statusbar.showMessage(txt)
        controller.selectionChanged.connect(onSelChanged)

        layout = QtGui.QHBoxLayout(container)
        container.setLayout(layout)
        layout.addWidget(label)
        layout.addWidget(textbox)
        layout.addWidget(button)
        window.setCentralWidget(container)

        return window

    def _pytest():
        import random

        controller = HierarchyConverterController()
        def nextsel():
            return random.choice([
                [],
                ['single'],
                ['single', 'double']
            ])

        def onconvert(prefix):
            print 'Convert clicked! Prefix:', prefix
            controller.selectionChanged.emit(nextsel())

        app = QtGui.QApplication([])
        win = create_window(controller)
        win.convertClicked.connect(onconvert)
        win.show()
        app.exec_()

    if __name__ == '__main__':
        _pytest()
#version5()

def version6():
    """Adds parent support."""

    class HierarchyConverterController(QtCore.QObject):
        selectionChanged = Signal(list)

    class ConverterWindow(QtGui.QMainWindow):
        convertClicked = Signal(str)

    def create_window(controller, parent=None):
        window = ConverterWindow(parent)
        window.setWindowTitle('Hierarchy Converter')
        statusbar = window.statusBar()

        container = QtGui.QWidget(window)
        label = QtGui.QLabel('Prefix:', container)
        textbox = QtGui.QLineEdit(container)
        button = QtGui.QPushButton('Convert', container)

        def onclick():
            window.convertClicked.emit(textbox.text())
        button.clicked.connect(onclick)

        def onSelChanged(newsel):
            if not newsel:
                txt = 'Nothing selected.'
            elif len(newsel) == 1:
                txt = '%s selected.' % newsel[0]
            else:
                txt = '%s objects selected.' % len(newsel)
            statusbar.showMessage(txt)
        controller.selectionChanged.connect(onSelChanged)

        layout = QtGui.QHBoxLayout(container)
        container.setLayout(layout)
        layout.addWidget(label)
        layout.addWidget(textbox)
        layout.addWidget(button)
        window.setCentralWidget(container)

        return window

    def _pytest():
        import random

        controller = HierarchyConverterController()
        def nextsel():
            return random.choice([
                [],
                ['single'],
                ['single', 'double']
            ])

        def onconvert(prefix):
            print 'Convert clicked! Prefix:', prefix
            controller.selectionChanged.emit(nextsel())

        app = QtGui.QApplication([])
        win = create_window(controller)
        win.convertClicked.connect(onconvert)
        win.show()
        app.exec_()

    if __name__ == '__main__':
        _pytest()
version6()
