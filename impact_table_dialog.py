# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'impact_table.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlgImpacts(object):
    def setupUi(self, dlgimp):
        dlgimp.setObjectName("dlgimp")
        dlgimp.resize(565, 354)
        self.tbImpacts = QtWidgets.QTableWidget(dlgimp)
        self.tbImpacts.setGeometry(QtCore.QRect(15, 11, 541, 331))
        self.tbImpacts.setAlternatingRowColors(True)
        self.tbImpacts.setObjectName("tbImpacts")
        self.tbImpacts.setColumnCount(3)
        self.tbImpacts.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbImpacts.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbImpacts.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbImpacts.setHorizontalHeaderItem(2, item)

        self.retranslateUi(dlgimp)
        QtCore.QMetaObject.connectSlotsByName(dlgimp)

    def retranslateUi(self, dlgimp):
        _translate = QtCore.QCoreApplication.translate
        dlgimp.setWindowTitle(_translate("dlgimp", "Impact Table"))
        item = self.tbImpacts.horizontalHeaderItem(0)
        item.setText(_translate("dlgimp", "Project"))
        item = self.tbImpacts.horizontalHeaderItem(1)
        item.setText(_translate("dlgimp", "Type"))
        item = self.tbImpacts.horizontalHeaderItem(2)
        item.setText(_translate("dlgimp", "Distance"))
