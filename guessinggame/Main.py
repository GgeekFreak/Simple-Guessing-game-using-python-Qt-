from threading import Timer
from PyQt5 import QtCore, QtGui, QtWidgets
from guessingmainwindow import Ui_Form
import sys

class mainwindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(mainwindow,self).__init__()
        self.initui()
    def initui(self):
        self.guess_count = 0
        self.setupUi(self)
        msg = QtWidgets.QMessageBox.information( self,"Guessing game", "The following game is a called guessing game. You must try to get "
                                                   "the secret word in order to pass the game.After 10 seconds a hint will "
                                                   "appear in the bottom to help you and remember you have only"
                                                   "eight trials , then you will lose .... good luck and have fun :)")
        self.label_count.setText("0")
        self.result_label.setVisible(0)
        self.hint_label.setVisible(0)
        self.logo_face.setVisible(0)
        self.timer = Timer(60, self.hints)
        self.guess_btn.clicked.connect(self.guess_game)
        self.timer.start()
    def hints(self):
        self.hint_label.setText("Hint: I am just like a woman , it is all about how you hold me ...\n but when i am angry i can"
                                " bring nightmares ")
        self.hint_label.setVisible(1)

    def guess_game(self):
        secret_word = "gun"
        guess_word = self.lineEdit.text()

        guess_limit = 8
        if len(guess_word) == 0:
            msg = QtWidgets.QMessageBox.critical(self,"Alert","you must enter a guessing word")
        else:

            if secret_word != guess_word:
               self.guess_count += 1
               self.label_count.setText(str(self.guess_count))
               self.lineEdit.setText("")
               if self.guess_count == guess_limit:

                  self.result_label.setText("You are out of guesses .. you lose")
                  self.label_count.setVisible(0)
                  self.lineEdit.setDisabled(1)
                  self.result_label.setVisible(1)

                  self.timer.cancel()

            else:
                self.result_label.setText("CONGRATS ... you have won the game")
                self.hint_label.setVisible(0)
                self.result_label.setVisible(1)
                self.logo_face.setVisible(1)
                self.timer.cancel()

if __name__ == '__main__':
   args = list(sys.argv)
   args[1:1] = ['-stylesheet', 'aqua.qss']
   app = QtWidgets.QApplication(args)
   win = mainwindow()
   win.show()
   app.exec()