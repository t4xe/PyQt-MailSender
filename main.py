#Mail Sender by t4xe
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit
import smtplib


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(499, 290)
        self.receiverLabel = QtWidgets.QLabel(Form)
        self.receiverLabel.setGeometry(QtCore.QRect(20, 20, 61, 20))
        self.receiverLabel.setObjectName("receiverLabel")
        self.subjectLabel = QtWidgets.QLabel(Form)
        self.subjectLabel.setGeometry(QtCore.QRect(20, 60, 61, 21))
        self.subjectLabel.setObjectName("subjectLabel")
        self.messageLabel = QtWidgets.QLabel(Form)
        self.messageLabel.setGeometry(QtCore.QRect(20, 100, 61, 21))
        self.messageLabel.setObjectName("messageLabel")
        self.senderLabel = QtWidgets.QLabel(Form)
        self.senderLabel.setGeometry(QtCore.QRect(300, 20, 47, 21))
        self.senderLabel.setObjectName("senderLabel")
        self.passwordLabel = QtWidgets.QLabel(Form)
        self.passwordLabel.setGeometry(QtCore.QRect(300, 50, 51, 21))
        self.passwordLabel.setObjectName("passwordLabel")
        self.sentOrErrorLabel = QtWidgets.QLabel(Form)
        self.sentOrErrorLabel.setGeometry(QtCore.QRect(110, 240, 250, 21))
        self.sentOrErrorLabel.setText("")
        self.sentOrErrorLabel.setObjectName("sentOrErrorLabel")
        self.receiverLineEdit = QtWidgets.QLineEdit(Form)
        self.receiverLineEdit.setGeometry(QtCore.QRect(70, 20, 121, 21))
        self.receiverLineEdit.setObjectName("receiverLineEdit")
        self.subjectLineEdit = QtWidgets.QLineEdit(Form)
        self.subjectLineEdit.setGeometry(QtCore.QRect(70, 60, 121, 21))
        self.subjectLineEdit.setObjectName("subjectLineEdit")
        self.messageTextEdit = QtWidgets.QTextEdit(Form)
        self.messageTextEdit.setGeometry(QtCore.QRect(70, 100, 121, 81))
        self.messageTextEdit.setObjectName("messageTextEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 240, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.senderLineEdit = QtWidgets.QLineEdit(Form)
        self.senderLineEdit.setGeometry(QtCore.QRect(350, 20, 113, 21))
        self.senderLineEdit.setObjectName("senderLineEdit")
        self.passwordLineEdit = QtWidgets.QLineEdit(Form)
        self.passwordLineEdit.setGeometry(QtCore.QRect(350, 50, 113, 21))
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        #self.showPasswordBox = QtWidgets.QCheckBox(Form)
        #self.showPasswordBox.setGeometry(QtCore.QRect(300, 80, 111, 17))
        #self.showPasswordBox.setObjectName("showPasswordBox")

        self.pushButton.clicked.connect(self.sendMail)
            
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        
        #if self.showPasswordBox.isChecked():
            #self.passwordLineEdit.setEchoMode(QLineEdit.NoEcho)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Mail Sender"))
        self.receiverLabel.setText(_translate("Form", "Receiver:"))
        self.subjectLabel.setText(_translate("Form", "Subject:"))
        self.messageLabel.setText(_translate("Form", "Message:"))
        self.senderLabel.setText(_translate("Form", "Sender:"))
        self.passwordLabel.setText(_translate("Form", "Password:"))
        self.pushButton.setText(_translate("Form", "Send"))
        #self.showPasswordBox.setText(_translate("Form", "Show Password"))      
   
    def sendMail(self):
        firstLen = len(self.receiverLineEdit.text())
        secondLen = len(self.messageTextEdit.toPlainText())
        thirdLen = len(self.subjectLineEdit.text())
        fourthLen = len(self.senderLineEdit.text())
        fifthLen = len(self.passwordLineEdit.text())
        
        if firstLen and secondLen and thirdLen and fourthLen and fifthLen != 0:
            try: 
                sender = self.senderLineEdit.text()
                password = self.passwordLineEdit.text()
                receiver = self.receiverLineEdit.text()
                subject = self.subjectLineEdit.text()
                messageText = self.messageTextEdit.toPlainText()
                
                smtp = smtplib.SMTP('smtp.gmail.com', 587) 
                smtp.starttls() 
                
                smtp.login(sender, password)               
                message = ("Subject: " + subject + "\n" + messageText)         
                smtp.sendmail(sender, receiver, message)
                     
                self.sentOrErrorLabel.setText("Email sent!")
                smtp.quit()
                
            except Exception as e:
                self.sentOrErrorLabel.setText("An error occured. Please read the console.")
                print(e)
        else:
            self.sentOrErrorLabel.setText("Please fill all fields.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
