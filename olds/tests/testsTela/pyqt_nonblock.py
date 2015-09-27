'''Setup for non-blocking PyQt apps

Routine Listings
----------------
There are two interfaces:
    pyqtapplication: Functional interface that returns the QApplication instance
    PyQtNonblock: Class that ensures the QApplication instance never goes out-of-scope

Usage
-----
The main class inherits PyQtNonblock, ensuring it is calling super().__init__
The module, if called as __main__, should, after instantiation of the main class,
explicitly execute the QApplication with instance.qapplication.exec_()
'''

class PyQtNonblock(object):
    '''Provide a standard interface for non-blocking Qt apps.

    Parameters
    ----------
    argv: list
          The command line arguments to pass to QApplication

    Attributes
    ----------
    qapplication: QApplication (class attribute only)
                 The instance of the QApplication
    '''

    qapplication = None

    def __init__(self, argv=None):
        self.__class__.qapplication = pyqtapplication(argv)

def pyqtapplication(argv=None):
    '''Return the current QApplication instance. If there is not one, one will be started

    Parameters
    ----------
    argv: list
          The command line arguments to pass to QApplication

    Returns
    -------
    QApplication:
        The current instance QApplication instance. If None, something
        didn't work
    '''
    from PyQt4.QtGui import QApplication

    qapplication = QApplication.instance()
    if not qapplication:
        argv = argv if argv else []
        qapplication = QApplication(argv)
    return qapplication
