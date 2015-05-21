import sys
from PySide import QtGui

class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        grid = QtGui.QGridLayout()

        exitAction = QtGui.QAction(QtGui.QIcon('inti logo text.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar().showMessage('Ready')

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.resize(500, 400)
        self.center()
        self.setWindowIcon(QtGui.QIcon('inti logo no text.png'))
        self.setWindowTitle('My Music on YouTube')
        self.show()
        
    def center(self):
        
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

