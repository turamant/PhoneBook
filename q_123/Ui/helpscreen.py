# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helpscreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HelpScreenDialog(object):
    def setupUi(self, HelpScreenDialog):
        HelpScreenDialog.setObjectName("HelpScreenDialog")
        HelpScreenDialog.resize(1178, 798)
        self.widget = QtWidgets.QWidget(HelpScreenDialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1181, 801))
        self.widget.setMinimumSize(QtCore.QSize(831, 731))
        self.widget.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.widget.setObjectName("widget")
        self.helpLabelWelcom = QtWidgets.QLabel(self.widget)
        self.helpLabelWelcom.setGeometry(QtCore.QRect(250, 20, 741, 131))
        self.helpLabelWelcom.setStyleSheet("font: 28pt \"DejaVu Math TeX Gyre\";\n"
"color: black;")
        self.helpLabelWelcom.setObjectName("helpLabelWelcom")
        self.errorLabel = QtWidgets.QLabel(self.widget)
        self.errorLabel.setGeometry(QtCore.QRect(380, 390, 461, 71))
        self.errorLabel.setStyleSheet("color: red;\n"
"font: 14pt \"Cantarell\";")
        self.errorLabel.setText("")
        self.errorLabel.setObjectName("errorLabel")
        self.helpCancelPushButton = QtWidgets.QPushButton(self.widget)
        self.helpCancelPushButton.setGeometry(QtCore.QRect(520, 730, 211, 51))
        self.helpCancelPushButton.setStyleSheet("border-radius:20px;\n"
"font: 18pt \"Cantarell\";\n"
"background-color: red;")
        self.helpCancelPushButton.setObjectName("helpCancelPushButton")
        self.helpTextEdit = QtWidgets.QTextEdit(self.widget)
        self.helpTextEdit.setGeometry(QtCore.QRect(30, 130, 551, 571))
        self.helpTextEdit.setObjectName("helpTextEdit")
        self.helptextEdit_2 = QtWidgets.QTextEdit(self.widget)
        self.helptextEdit_2.setGeometry(QtCore.QRect(630, 130, 521, 571))
        self.helptextEdit_2.setObjectName("helptextEdit_2")

        self.retranslateUi(HelpScreenDialog)
        QtCore.QMetaObject.connectSlotsByName(HelpScreenDialog)

    def retranslateUi(self, HelpScreenDialog):
        _translate = QtCore.QCoreApplication.translate
        HelpScreenDialog.setWindowTitle(_translate("HelpScreenDialog", "Dialog"))
        self.helpLabelWelcom.setText(_translate("HelpScreenDialog", "Справочник по PhoneBook"))
        self.helpCancelPushButton.setText(_translate("HelpScreenDialog", "Выход"))
        self.helpTextEdit.setHtml(_translate("HelpScreenDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\">\n"
"<tr>\n"
"<td>\n"
"<h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"сценарий-использования\"></a><span style=\" font-size:medium; font-weight:600;\">С</span><span style=\" font-size:medium; font-weight:600;\">ценарий использования:</span></h4>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\"\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Пользователь включает программу, перед ним появляется окно авторизации ( при первом входе. При включенном чекбоксе – «Запомнить меня» необходимо входить автоматически)</li>\n"
"<li style=\"\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Пользователь вводит логин и пароль, нажимает кнопку «Войти». В случае нахождения пользователя с такой комбинацией программа переходит к главному меню, в случае отсутствия появляется всплывающее окно «Пользователь с такими данными не найден»</li>\n"
"<li style=\"\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Если пользователь забыл пароль – по нажатию на ссылку «Забыли пароль?» открывается окно «Восстановление пароля»</li>\n"
"<li style=\"\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">При нажатии на кнопку «Регистрация» открывается окно «Регистрация»</li>\n"
"<li style=\"\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">В случае успешного входа/регистрации перед пользователем открывается главное окно с навигацией по Алфавиту.</li></ol>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"список-требований-к-программе\"></a><span style=\" font-size:medium; font-weight:600;\">С</span><span style=\" font-size:medium; font-weight:600;\">писок требований к программе:</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\"\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">В программе должна быть реализована функция напоминаний ( при открытии программы необходимо показывать список именинников на ближайшую неделю)</li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">В программе должны быть реализованы функции:<br />• Добавление нового контакта<br />• Редактирование существующего контакта<br />• Удаление существующего контакта</li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">В программе должен быть логический контроль дубликатов ( программа должна запрещать записывать нового пользователя, если совпадает ФИО + дата рождения + номер телефона)</li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Программа должна автоматически переносить созданную запись на нужную страницу в алфавитном указателе и информировать об этом пользователя) </li></ol>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"стек-используемых-технологий\"></a><span style=\" font-size:medium; font-weight:600;\">С</span><span style=\" font-size:medium; font-weight:600;\">тек используемых технологий:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PyQt5 + python3.9.6; в качестве СУБД использовать Mariadb 10.4 и выше.<br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">В качестве решения предоставлена ссылка на репозиторий, </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/turamant/PhoneBook\"><span style=\" text-decoration: underline; color:#0057ae;\">https://github.com/turamant/PhoneBook</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">а также подробную инструкцию по установке на <a href=\"https://github.com/turamant/PhoneBook\"><span style=\" text-decoration: underline; color:#0057ae;\">linux.</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></td>\n"
"<td></td></tr>\n"
"<tr>\n"
"<td></td>\n"
"<td></td></tr></table>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.helptextEdit_2.setHtml(_translate("HelpScreenDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Разъяснения:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">1. База данных</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    База данных состоит из двух таблиц:  &quot;phonebook&quot; и &quot;users&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Таблица &quot;phonebook&quot; - поля id(Int ,NN,PK,AI),</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                                                name(VarChar(100)),</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                                                nomer(Char(12)),</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                                                birthday (Date).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   Таблица &quot;users&quot;             - поля id(Int,NN,PK,AI),</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                                               email( VarChar(100)),</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                                               password(VarChar(100)),</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                                               save(Char(1)).</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">2. Пользователи (таблица &quot;users&quot;)  делятся на два типа:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    - admin  (добавлять, изменять, удалять записи в таблицах)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    - user - может просматривать данные из таблицы &quot;phonebook&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">3. Регистрация пользователей</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    - admin  - любой пароль</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    - пользователь (@email при регистрации) - любой пароль                                             </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">4. Запомнить меня</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    - При нажатии на чекбокс, происходит запись поля save таблицы &quot;users&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    -  Запуск программы будет автоматичесим для первого из запоменных    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        пользователей. </p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HelpScreenDialog = QtWidgets.QDialog()
    ui = Ui_HelpScreenDialog()
    ui.setupUi(HelpScreenDialog)
    HelpScreenDialog.show()
    sys.exit(app.exec_())